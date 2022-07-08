from django.urls import path
from .views import NewsPage

app_name = 'news'

urlpatterns = [
    path('', NewsPage.as_view(), name='news-page'),
]
