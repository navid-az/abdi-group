from django.shortcuts import render
from django.views import View
from .models import News

class NewsPage(View):
  def get(self, request):
    news = News.objects.all()
    return render(request, 'news-page.html', {'news':news})

class NewsDetail(View):
  def get(self, request, id):
    news = News.objects.get(id=id)
    return render(request, 'news.html', {'news':news})