from django.db import models

from accounts.models import User


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS = (
        ('a', 'awaiting moderation'),
        ('r', 'rejected'),
        ('p', 'published'),
    )
    status = models.CharField(choices=STATUS, max_length=1, default='a')
    title = models.CharField(max_length=250)
    text = models.TextField()
    topics = models.ManyToManyField(Topic)
    tags = models.ManyToManyField(Tag)
    date_time_publication = models.DateTimeField(auto_now_add=True)
    number_views = models.IntegerField(default=0)

    def __str__(self):
        return "{} ({})".format(self.title, self.get_status_display())

    class Meta:
        permissions = (
            ('can_change_status', 'Can change post status'),
            ('can_see_non_published_posts', 'Can see non published posts'),
        )


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_time_publication = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return self.user.username
