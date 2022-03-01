from os import name
from django.urls import path
from .views import capabilities

app_name = 'capabilities'

urlpatterns = [
    path('', capabilities, name='capabilities' )
]