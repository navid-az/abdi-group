from django.urls import path
from .views import NewsPage, NewsDetail

app_name = 'news'

urlpatterns = [
    path('', NewsPage.as_view(), name='news-page'),
    path('<int:id>/', NewsDetail.as_view(), name='news-detail')
]
