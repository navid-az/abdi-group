from django.urls import path
from .views import mr_dr

app_name= 'mr-dr'

urlpatterns = [
    path('', mr_dr, name='mr-dr')
]
