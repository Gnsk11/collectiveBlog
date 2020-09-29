from django.contrib import admin
from .models import Post, Tag, Topic, Comment, Favorite

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Favorite)
