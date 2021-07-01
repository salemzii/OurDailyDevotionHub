from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    POST_CATEGORY = (
        ('devotion', 'DEVOTION'),
        ('regular', 'REGULAR')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=120, choices=POST_CATEGORY)
    title = models.CharField(max_length=210)
    content = models.TextField()

    def __str__(self):
        template = f"{self.title}"
        return template.format(self)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', null=True)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['date']

    def __str__(self):
        return self.user.username


class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='bookmarks')

    class meta:
        ordering = ['-date']

    def __str__(self):
        template = f"{self.user.username}'s bookmark"
        return template.format(self)

# Create your models here.
