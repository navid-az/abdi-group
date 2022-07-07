from django.db import models
from pytz import timezone

# Create your models here.
class MrDr(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=100)
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.email