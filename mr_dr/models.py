import email
from django.db import models

# Create your models here.
class MrDr(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    body = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)