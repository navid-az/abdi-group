from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from jalali_date import datetime2jalali, date2jalali

class News(models.Model):
  title = models.CharField(max_length=250, blank=True, null=True)
  summery = RichTextField(blank=True, null=True)
  image = models.ImageField(upload_to='news-images/%Y/%m/%d/', blank=True, null=True)
  body = RichTextField(blank=True, null=True)
  created = models.DateTimeField(auto_now=True, blank=True, null=True)

  def __str__(self):
    return self.title

  def jalali_date(self):
    return date2jalali(self.created)
