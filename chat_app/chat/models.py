from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(default='Room Name', max_length=1000)

class Message(models.Model):
    text = models.CharField(default='text', max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(default='text', max_length=10000)
    room = models.CharField(default='text', max_length=10000)
 