from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(default='name', max_length=1000)
    age = models.IntegerField(default=0)
    date_enrolled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name