from django.shortcuts import render

# Create your views here.

def capabilities(request):
    return render(request, 'capabilities/capabilities.html' )
