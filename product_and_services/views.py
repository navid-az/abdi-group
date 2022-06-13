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

def ffs_ftp(request):
    return render(request, 'product_and_services/oil_and_gas/ffs_ftp.html')

def leak_detection(request):
    return render(request, 'product_and_services/oil_and_gas/leak_detection.html')

def valve_clinic(request):
    return render(request, 'product_and_services/oil_and_gas/valve_clinic.html')

def inspection(request):
    return render(request, 'product_and_services/oil_and_gas/inspection.html')

def civil_projects(request):
    return render(request, 'product_and_services/civil_projects.html')

def process_units(request):
    return render(request, 'product_and_services/process_units.html')