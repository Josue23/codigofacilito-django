from django.db import models
from adopcion.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)


class Mascota(models.Model):
    folio = models.CharField(max_length=10, blank=True, primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    edad_aproximada = models.IntegerField()
    fecha_resgate = models.DateField()
    persona = models.ForeignKey(Persona, related_name='mascotas', null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, related_name='vacunas')
