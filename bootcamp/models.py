from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
#id--> autoincrement
#first_name --> string
#last_name  --> string
#generation --> string
#email --> string
#phone --> status -->(activo, dado de bajja)
#address --> string
#size --> (s, m, l)
#created_at --> date
#updated_at --> date


#las clases(modelos) van capitalizadas --> koder
#Los modelos heredan del modelo predetermiando de Django
#Cada modelo representa una tabla de sql
#Cada propiead de la clase(modelo) representa un atgributo en la tabla

class Bootcamp(models.Model):
    """Bootcam model."""
    name = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.name}" 
class Generation(models.Model):
    """Generation model."""
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
     
    #Foreign Key
    bootcamp = models.ForeignKey(Bootcamp, models.PROTECT, related_name="generations")
     
    def __str__(self):
         return f"numero -> {self.number} {self.bootcamp.name}"

#Koders pertenece a 1 generacion -> 1 generation - N Koders    
class Koder(models.Model):
    """koder Model."""
    STATUSES = [
        ("active","Active"),
        ("inactive", "Inactive"),
        ("finished", "Finished"),
    ]
    
    first_name = models.CharField(max_length=255)  #-->string
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    status = models.CharField(max_length=8,choices=STATUSES, default="active")
    created_at = models.DateTimeField(auto_now_add = True) # -->en cuanto se cree nos agrega la hora por automatico.
    
    #Foreing Keys
    generation = models.ForeignKey(Generation,models.PROTECT,related_name="koders")
      
    #Representar como nos regresan al Koder.
    
    def __str__(self):
        return f"firstName -> {self.first_name}, lastName -> {self.last_name}"
    

# 
class Mentor(models.Model):
     
    """Mentor Model."""
    
    first_name = models.CharField(max_length=255)  #-->string
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True) # -->en cuanto se cree nos agrega la hora por automatico.
    # Foreign Keys
    generations = models.ManyToManyField(Generation, related_name = "mentors")

    def __str__(self):
        return f"id: {self.pk}  {self.first_name} {self.last_name}"
 
 
#Koders pertenece a 1 generacion -> 1 generation - N Koders
#Mentores pertenece a varias generaciones -> N mentors -N generaciones 
#Koders pertenece a 1 generacion -> 1 generation - N Koders

#..........................................................
# #class Koder_ant(models.Model):
#    STATUSES = [
#        ("active","Active"),
#        ("inactive", "Inactive"),
#        ("finished", "Finished"),
#    ]
#    SIZES =[
#        ("s", "Small"),
#        ("m", "Medium"),
#        ("l", "Large"),
#    ]
#    first_name = models.CharField(max_length=255)  #-->string
#    last_name = models.CharField(max_length=255)
#    generation = models.CharField(max_length=20)
#    email = models.EmailField(unique=True)
#    phone = models.CharField(max_length=25)
#    status = models.CharField(max_length=8,choices=STATUSES, default="active")
#    size = models.CharField(max_length=1, choices=SIZES, default="m")
#    birthdate = models.DateTimeField()
#    created_at = models.DateTimeField(auto_now_add = True) # -->en cuanto se cree nos agrega la hora por automatico.
 #   updated_at = models.DateField(blank=True, null=True)