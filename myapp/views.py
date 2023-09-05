from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#Importar HHTTP response
from  django.http import HttpResponse
from django.template import  loader
# Create your views here.

#El cliente -> pide ->requests
#El Servidor -> Responde
def bienvenida(request):
    #Responder
    return  HttpResponse("Bienvenido")
    
def despedida(request):
    #Responder
    return  HttpResponse("Adios")

def saludo(request):
    #saludo a koder
    return HttpResponse("Hola koders")

def saludo_con_nombre(request,name):
    context={#"nombre": name}
             "apellido":"Llamas"}
    template = loader.get_template("templates/base.html")  #Va a servir para pasarle info al templates
    #1print("lo que yo imprimo es en mi terminar-->",name)
    return HttpResponse(template.render(context,request))
    #1return HttpResponse(f"Hola {name}")
    
def saludo_tipo(request,name,typ):
    context={"nombre": name,"tipo":typ}
    template = loader.get_template("templates/tipo.html")  #Va a servir para pasarle info al templates
    #1print("lo que yo imprimo es en mi terminar-->",name)
    return HttpResponse(template.render(context,request))
    #1return HttpResponse(f"Hola {name}")

def kodemia_mentor(request,tipo):
    if tipo == "mentor":
        print("Hello mentor here are your casses")
        mensaje="Hello mentor here are your casses"
    elif tipo == "koder":
        print("Hello Koder welcome to kodemia")
        mensaje="Hello Koder welcome to kodemia"
    else:
        print("You are not welcome here")
        mensaje = "You are not welcome here"
    return HttpResponse(mensaje)     

