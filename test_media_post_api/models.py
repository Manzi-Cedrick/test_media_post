from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    scheduled_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    shares = models.IntegerField(default=0, blank=True)
    comments = models.IntegerField(default=0, blank=True)
    draft = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.title
