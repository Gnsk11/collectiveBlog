from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),

    path('post/add', views.AddPost.as_view(), name='add_post'),
    path('post/add/successfully', views.AddPostSuccessfully.as_view(), name='add_post_successfully'),
    path('post/<int:post_id>/comment/add', views.AddComment.as_view(), name='add_comment'),
    path('post/<int:pk>', views.PostView.as_view(), name='post_view'),
    path('post/<int:pk>/to_favorites', views.PostToFavorites.as_view(), name='to_favorites'),

    path('posts', views.PostsView.as_view(), name='posts'),
    path('posts/topic/<str:topic_name>', views.PostsView.as_view(), name='topic_posts'),
    path('posts/tag/<str:tag_name>', views.PostsView.as_view(), name='tag_posts'),

    path('moderate/posts', views.ModeratorPostsView.as_view(), name='moderate_posts'),
    path('moderate/<int:post_id>/reject', views.PostReject.as_view(), name='post_reject'),
    path('moderate/<int:pk>', views.UpdatePost.as_view(), name='post_update'),
]
