from django.shortcuts import render
from django.views import View

class NewsPage(View):
  def get(self, request):
    return render(request, 'news-page.html')