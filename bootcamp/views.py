from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#Importar HHTTP response
from  django.http import HttpResponse
# Create your views here.
from django.template import loader
from bootcamp.models import Koder

def get_koder(request,koder_id):
    koders=Koder.objects.filter(pk=koder_id)
    return HttpResponse(koders)

def get_koder_ant(request,koder_id):
    koders = [
        {"koder_id": 1,
         "name": "Miren",
         "last_name":"Llamas"},
        {"koder_id": 2,
         "name": "Fernando",
         "last_name":"Fernandez"},
        {"koder_id": 3,
         "name": "Rodrigo",
         "last_name":"Rodriguez"},
        ]
    koder_buscado = [koder for koder in koders if koder["koder_id"]==koder_id]
    return HttpResponse(f"tu koders:{koder_buscado}")


def list_koders(request):
    koders = Koder.objects.all()
    return HttpResponse(koders)

def list_Koders_ant(request):
    context={
        "bootcamp": {"name": "Python", "module":"Django"},
        "koders" : [
                {"name": "Miren","last_name":"Llamas","generation":"1g","is_active":True},
                {"name": "Fernando","last_name":"Fernandez","generation":"1g","is_active":True},
                {"name": "Rodrigo","last_name":"Rodriguez","generation":"1g","is_active":False},
        ],
    }
    template =loader.get_template("templates/list_Koders.html")
     #return HttResponse(koders) 
    return HttpResponse(template.render(context,request))
      
def list_mentors(request):
    context ={
        "mentors": [
            {
                "name": "Benjamin",
                "last_name": "Aguilar",
                "is_active": True
            },
            {
                "name": "Alfredo",
                "last_name": "Altamirano",
                "is_active": True
            },
            {
                "name": "Charles",
                "last_name": "Lopez",
                "is_active": False
            },
        ]
       
    }

    template =loader.get_template("templates/list_mentors.html")
    return HttpResponse(template.render(context,request))