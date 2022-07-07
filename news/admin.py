from django.contrib import admin
from .models import News
# from jalali_date import datetime2jalali, date2jalali
# from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	

# Register your models here.

# @admin.register(News)
admin.site.register(News)
# class NewsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
	
	
#def get_created_jalali(self, obj):
#return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
