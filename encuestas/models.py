# -*- coding: UTF-8 -*-

from django.db import models
from maonic.lugar.models import *
from django.contrib.auth.models import User
from maonic.mapeo.models import *

# Create your models here.

class Recolector(models.Model):
    nombre = models.CharField("Nombre del recolector", max_length=200,
                              help_text="Introduzca el nombre del recolector",
                              )
    class Meta:
        verbose_name_plural = "Recolector"
    def __unicode__(self):
        return self.nombre
SEXO = (
            (1,"Masculino"),
            (2,"Femenino")
       )
CHOICE_OPCION = (
                    (1,"Si"),
                    (2,"No")
                )
                       
class Encuesta(models.Model):
    fecha = models.DateField()
    recolector = models.ForeignKey(Recolector)
    productor = models.ForeignKey(Familia)
    sexo = models.IntegerField(choices=SEXO)
    edad = models.IntegerField('Edad del productor')
    #usuario que va a digitar la encuestas
    usuario = models.ForeignKey(User)
    
    class Meta:
        verbose_name_plural = "Encuestas monitoreo MAONIC"
    def __unicode__(self):
        return self.productor.nombre
