from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=70, blank=True, null=True)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    domicilio = models.TextField()