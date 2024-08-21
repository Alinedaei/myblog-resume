# blog/models.py
from django.db import models
from django.contrib.auth.models import User  # یا مدل کاربری دلخواه شما

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # اطمینان از تعریف صحیح
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

