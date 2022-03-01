from os import name
from django.urls import path
from .views import company

app_name = 'company'

urlpatterns = [
    path('', company, name='company' )
]
