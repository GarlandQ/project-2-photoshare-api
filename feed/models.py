from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='posts')
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)
