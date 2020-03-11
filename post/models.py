from django.db import models
from django.contrib.auth.models import User
from textbook.models import Post
# Create your models here.
class Message(models.Model):
    message = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
