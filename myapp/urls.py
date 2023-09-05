from django.contrib import admin
from django.urls import path

#Viws
from .views import bienvenida, despedida, saludo, saludo_con_nombre,kodemia_mentor,saludo_tipo

#  ruta  ->  http://127.0.0.1:8000/

urlpatterns = [
    path("", bienvenida),
    path("despedida/", despedida),
    path("saludo/",saludo),
    path("saludo/<str:name>",saludo_con_nombre),
    path("kodemia/<str:tipo>",kodemia_mentor),
    path("saludotipo/<str:name>,<str:typ>", saludo_tipo),
]
