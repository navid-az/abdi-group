from django.shortcuts import render
from .models import MrDr

def mr_dr(request):
    questions = MrDr.objects.all()
    return render(request, 'mr_dr/mr_dr.html',{'questions':questions})
