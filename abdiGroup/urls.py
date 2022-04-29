from argparse import Namespace
from os import name
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [path('i18n/', include('django.conf.urls.i18n')),]

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('capabilities.urls', namespace='home')),
    path('capabilities/', include('capabilities.urls', namespace='capabilities')),
    path('product-and-services/', include('product_and_services.urls', namespace ='product-and-services')),
    path('company', include('company.urls', namespace='company')),
    path('mr-dr', include('mr_dr.urls', namespace='mr-dr')),
)
