from blog.models import Post, Favorite
from .models import User


def get_user(user_id):
    return User.objects.filter(id=user_id)


def get_user_posts(user_id, status=None):
    return Post.objects.filter(user_id=user_id, status=status).order_by('date_time_publication').reverse()


def create_favorite(user_id):
    favorite = Favorite(user_id=user_id)
    favorite.save()


def get_favorites(user_id):
    favorite = Favorite.objects.get(user_id=user_id)
    return favorite.posts.all()
