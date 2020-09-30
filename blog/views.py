from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from . import services
from .models import Post, Comment


class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'topics', 'tags']
    success_url = reverse_lazy('add_post_successfully')
    template_name = 'blog/add_post.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class UpdatePost(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'topics', 'tags']
    success_url = reverse_lazy('moderate_posts')
    template_name = 'blog/moderator/post_update.html'
    permission_required = (
        'blog.can_see_non_published_posts',
        'blog.can_change_status',
    )

    def form_valid(self, form):
        post = form.save(commit=False)
        post.status = 'p'
        post.save()
        return super().form_valid(form)


class AddPostSuccessfully(View):
    template_name = 'blog/add_post_successfully.html'

    def get(self, request):
        return render(request, self.template_name)


class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'blog/add_comment.html'

    def get_success_url(self):
        return reverse('post_view', kwargs={'pk': self.kwargs['post_id']})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['post_id']
        form.instance.sender_id = self.request.user.id
        return super().form_valid(form)


class PostView(DetailView):
    model = Post

    def get_queryset(self):
        return services.get_verified_post(self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['comments'] = services.get_comments(post_id=self.kwargs['pk'])
        context['previous_page'] = self.request.META['HTTP_REFERER']
        return context


class PostsView(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        topic_name = self.kwargs.get('topic_name', None)
        tag_name = self.kwargs.get('tag_name', None)
        return services.get_verified_posts(topic_name=topic_name, tag_name=tag_name)

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['topics'] = services.get_topics()
        return context


class ModeratorPostsView(PermissionRequiredMixin, ListView):
    permission_required = 'blog.can_see_non_published_posts'
    model = Post
    paginate_by = 20
    template_name = 'blog/moderator/post_list.html'

    def get_queryset(self):
        return services.get_non_verified_posts()


class PostReject(PermissionRequiredMixin, View):
    permission_required = 'blog.can_change_status'

    def get(self, request, post_id):
        services.reject_post(post_id)
        return redirect('moderate_posts')


class PostToFavorites(LoginRequiredMixin, View):

    def get(self, request, pk):
        services.add_post_to_favorites(post_id=pk, user_id=request.user.id)
        return redirect(request.META.get('HTTP_REFERER'))


class PostUnFavorites(LoginRequiredMixin, View):

    def get(self, request, pk):
        services.delete_post_in_favorites(post_id=pk, user_id=request.user.id)
        return redirect(request.META.get('HTTP_REFERER'))


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post

    def get_object(self, queryset=None):
        obj = super(DeletePost, self).get_object()
        if obj.user.id != self.request.user.id:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse('account', kwargs={
            'pk': self.request.user.id,
            'status': 'p',
        })
