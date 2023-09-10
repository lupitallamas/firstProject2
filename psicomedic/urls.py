from django.urls import path

from .views import list_psychologist, get_psychologist, list_patients, get_patient, list_appointments, get_appointment
#  ruta  ->  http://127.0.0.1:8000/

urlpatterns = [
    path("psychologists/", list_psychologist),  
    path("psychologists/<int:psychologist_id>", get_psychologist), 
    path("patients/", list_patients),
    path("patients/<int:patient_id>", get_patient),
    path("appointments/", list_appointments),
    path("appointments/<int:appointments_id>", get_appointment),
]