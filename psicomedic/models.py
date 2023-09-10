from django.db import models

# Create your models here.

class Psychologist(models.Model):
    """Psychologist model."""
    
    first_name = models.CharField(max_length=255)  #-->string
    last_name = models.CharField(max_length=255)
    birthdate = models.DateTimeField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True) # -->en cuanto se cree nos agrega la hora por automatico
     
    #Foreign Key
     
    def __str__(self):
        return f"Psicologo {self.first_name} {self.last_name}"
     
class Patient(models.Model):
    """Patient model."""
    
    first_name = models.CharField(max_length=255)  #-->string
    last_name = models.CharField(max_length=255)
    birthdate = models.DateTimeField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    biography=models.CharField(max_length=255)
    address_id=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True) # -->en cuanto se cree nos agrega la hora por automatico
        
    #Foreign Key
        
    def __str__(self):
        return f" {self.first_name} {self.last_name}"
    
class Appointment(models.Model):
    """Appoimtment model. """
    
    appointment_date = models.DateTimeField()
    #patient_id = models.IntegerField()
    #phychologist_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
        
    #Foreign Key
    pychologist = models.ForeignKey(Psychologist, models.PROTECT, related_name="appointments")
    patient = models.ForeignKey(Patient, models.PROTECT, related_name="appointments")

    def __str__(self):
        return f"{self.patient.id}  {self.pychologist.id} "
