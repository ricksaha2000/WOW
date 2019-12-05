from django.db import models
from django.contrib.auth.models import User


class Community(models.Model):
    title = models.CharField(max_length=120)
    user = models.OneToOneField(User, max_length=120, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    community = models.CharField(max_length=120)
    comment = models.CharField(max_length=1200)
    user = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

