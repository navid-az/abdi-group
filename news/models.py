from django.db import models
# from ckeditor.fields import RichTextField
from jalali_date import datetime2jalali, date2jalali

class News(models.Model):
  title = models.CharField(max_length=250, default='hello')
  summery = models.TextField()
  main_image = models.ImageField(upload_to='news-images/')
  body = models.TextField()
  created = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  def jalali_date(self):
    return date2jalali(self.created)
