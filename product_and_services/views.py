from django.shortcuts import render

# Create your views here.

def inline_inspections(request):
    return render(request, 'product_and_services/inline_inspection.html')


def cathodic_protection(request):
    return render(request, 'product_and_services/cathodic_protection.html')

def under_water_inspection(request):
    return render(request, 'product_and_services/under_water_inspection.html')

def cleaning_pigs(request):
    return render(request, 'product_and_services/cleaning_pigs.html')

def unpigable_pipelines(request):
    return render(request, 'product_and_services/unpigable_pipelines.html')