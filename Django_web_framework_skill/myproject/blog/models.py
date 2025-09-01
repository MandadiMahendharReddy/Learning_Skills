from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)  # once at creation
    updated_at = models.DateTimeField(auto_now=True)      # updates on save

    def __str__(self):
        return self.title

