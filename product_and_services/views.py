from django.shortcuts import render

# Create your views here.

def inline_inspections(request):
    return render(request, 'product_and_services/oil_and_gas/inline_inspection.html')


def cathodic_protection(request):
    return render(request, 'product_and_services/oil_and_gas/cathodic_protection.html')

def under_water_inspection(request):
    return render(request, 'product_and_services/oil_and_gas/under_water_inspection.html')

def cleaning_pigs(request):
    return render(request, 'product_and_services/oil_and_gas/cleaning_pigs.html')

def unpigable_pipelines(request):
    return render(request, 'product_and_services/oil_and_gas/unpigable_pipelines.html')
    
def repairing(request):
    return render(request, 'product_and_services/oil_and_gas/repairing.html')