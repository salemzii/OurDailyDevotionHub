from django.contrib import admin
from .models import Like, Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)

# Register your models here.
