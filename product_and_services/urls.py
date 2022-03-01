import imp
from os import name
from django.urls import path
from .views import inline_inspections, cathodic_protection, under_water_inspection, cleaning_pigs, unpigable_pipelines

app_name = 'product-and-services'

urlpatterns = [
    path('inline-inspection/', inline_inspections, name='inline-inspection'),
    path('cathodic-protection/', cathodic_protection, name='cathodic-protection'),
    path('under-water-inspection/', under_water_inspection, name='under-water-inspection'),
    path('cleaning-pigs/', cleaning_pigs, name='cleaning-pigs'),
    path('unpigable-pipelines/', unpigable_pipelines, name='unpigable-pipelines'),
]
