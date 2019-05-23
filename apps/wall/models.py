from django.db import models
from apps.login.models import User

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages")
    message = models.TextField()
    like = models.ManyToManyField(User, related_name="liked_msgs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments")
    user = models.ForeignKey(User, related_name="comments")
    comment = models.TextField()
    like = models.ManyToManyField(User, related_name="liked_cmnts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)