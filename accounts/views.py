from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView

from blog.models import Favorite
from . import services
from .forms import RegistrationForm
from .models import User


class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        services.create_favorite(user.id)
        return super().form_valid(form)


class AccountView(LoginRequiredMixin, DetailView):
    model = User

    def get_queryset(self):
        return services.get_user(self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['posts'] = services.get_user_posts(user_id=self.kwargs['pk'], status=self.kwargs['status'])
        return context


class FavoritesView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'accounts/favorites.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.id == self.kwargs['pk']:
            return services.get_favorites(self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FavoritesView, self).get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        return context
