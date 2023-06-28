from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    date_created = models.DateTimeField(default=datetime.now())

    user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Like(models.Model):
    date_liked = models.DateTimeField(default=datetime.now())

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
