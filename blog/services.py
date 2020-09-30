from django.core.exceptions import ObjectDoesNotExist

from .models import Post, Comment, Topic, Favorite


def get_verified_post(post_id):
    queryset = Post.objects.filter(id=post_id, status='p')
    if queryset:
        post = queryset.get()
        post.number_views += 1
        post.save()
    return queryset


def get_verified_posts(topic_name, tag_name):
    queryset = Post.objects.filter(status='p').order_by('number_views', 'date_time_publication').reverse()
    if topic_name:
        queryset = queryset.filter(topics__name=topic_name)
    if tag_name:
        queryset = queryset.filter(tags__name=tag_name)
    return queryset


def get_comments(post_id):
    return Comment.objects.filter(post_id=post_id).order_by('date_time_publication').reverse()


def get_non_verified_posts():
    return Post.objects.filter(status='a').order_by('date_time_publication').reverse()


def reject_post(post_id):
    try:
        post = Post.objects.get(id=post_id, status='a')
        post.status = 'r'
        post.save()
        return True
    except ObjectDoesNotExist:
        return False


def get_topics():
    return Topic.objects.all()


def add_post_to_favorites(post_id, user_id):
    favorite = Favorite.objects.get(user_id=user_id)
    favorite.posts.add(Post.objects.get(id=post_id))
    favorite.save()


def delete_post_in_favorites(post_id, user_id):
    favorite = Favorite.objects.get(user_id=user_id)
    favorite.posts.remove(Post.objects.get(id=post_id))
    favorite.save()
