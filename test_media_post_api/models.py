from django.db import models
import uuid  
from django.conf import settings

class User(models.Model):
    username = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    title = models.CharField(max_length=100)
    description = models.TextField()
    scheduled_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    shares = models.IntegerField(default=0, blank=True)
    draft = models.BooleanField(default=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.comment
    
class Drafts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.post.title