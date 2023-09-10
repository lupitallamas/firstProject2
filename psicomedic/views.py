from django.shortcuts import render
# Create your views here.
#Importar HHTTP response
from  django.http import HttpResponse
from django.template import  loader
from psicomedic.models import Psychologist, Patient, Appointment

# Create your views here.


def list_psychologist(request):
    
    psychologist= Psychologist.objects.all()
     
    context = {"psychologists":  psychologist} 
    
    template =loader.get_template("templates/psicomedic/list_psychologist.html")
    # /Users/lupitallamas/django1/firstProject2/firstProject2/templates/psicomedic/list_psychologist.html
    
    return HttpResponse(template.render(context,request))



def get_psychologist(request,psychologist_id):
    
    psychologist = Psychologist.objects.filter(pk=psychologist_id)
    
    context = {"psychologists":  psychologist} 
     
    template =loader.get_template("templates/psicomedic/list_psychologist.html")
    # /Users/lupitallamas/django1/firstProject2/firstProject2/templates/psicomedic/list_psychologist.html
    
    return HttpResponse(template.render(context,request))

""".............. Patient Models.........."""

def list_patients(request):
    """Lista de pacientes"""
    patients= Patient.objects.all()
    context = {"patients":  patients} 
    template =loader.get_template("templates/psicomedic/list_patients.html")
    
    return HttpResponse(template.render(context,request))



def get_patient(request,patient_id):
    """Consuta de um paciente"""
    
    patient = Patient.objects.filter(pk=patient_id)
    context = {"patients": patient} 
    template =loader.get_template("templates/psicomedic/list_patients.html")
    
    return HttpResponse(template.render(context,request))

""".............. Approintments Models.........."""

def list_appointments(request):
    """ Lista de Appointment de appointments """
    
    appointment = Appointment.objects.all()
    context = {"appointments": appointment}
    template =loader.get_template("templates/psicomedic/list_appointment.html")
    
    return HttpResponse(template.render(context,request))

def get_appointment(request,appointments_id):
    """Una appoointment"""
    
    appointment = Appointment.objects.filter(pk=appointments_id)
    context = {"appointments": appointment}
    template =loader.get_template("templates/psicomedic/list_appointment.html")
    
    return HttpResponse(template.render(context,request))


