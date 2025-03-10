from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
    
    def __str__(self):
        return self.title
    
    