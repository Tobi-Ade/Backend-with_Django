from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(default='title',max_length=1000)
    content = models.CharField(default='blog post', max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
