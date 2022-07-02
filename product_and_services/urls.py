from django.urls import path
from .views import civil_projects, ffs_ftp, inline_inspections, cathodic_protection, under_water_inspection, cleaning_pigs, unpigable_pipelines, repairing, ffs_ftp, leak_detection, valve_clinic, inspection, process_units, industrial_technology, management_systems

app_name = 'product-and-services'

urlpatterns = [
    path('oil-and-gas-pipelines/inline-inspection/', inline_inspections, name='inline-inspection'),
    path('oil-and-gas-pipelines/cathodic-protection/', cathodic_protection, name='cathodic-protection'),
    path('oil-and-gas-pipelines/under-water-inspection/', under_water_inspection, name='under-water-inspection'),
    path('oil-and-gas-pipelines/cleaning-pigs/', cleaning_pigs, name='cleaning-pigs'),
    path('oil-and-gas-pipelines/unpigable-pipelines/', unpigable_pipelines, name='unpigable-pipelines'),
    path('oil-and-gas-pipelines/repairing/', repairing, name='repairing'),
    path('oil-and-gas-pipelines/ffs-ftp/', ffs_ftp, name='ffs-ftp'),
    path('oil-and-gas-pipelines/leak-detection/', leak_detection, name='leak-detection'),
    path('oil-and-gas-pipelines/valve-clinic/', valve_clinic, name='valve-clinic'),
    path('oil-and-gas-pipelines/inspection/', inspection, name='inspection'),

    path('civil-projects/', civil_projects, name='civil-projects'),
    path('process-units/', process_units, name='process-units'),
    path('industrial-technology/', industrial_technology, name='industrial-technology'),
    path('management-systems/', management_systems, name='management-systems'),
]
