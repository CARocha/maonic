# -*- coding: utf-8 -*-
from django.db import models
from encuestas.models import *

# Create your models here.
class Arboles(models.Model):
	nombre = models.CharField(max_length=250)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Arbol'
		verbose_name_plural = 'Arboles'

class InventarioForestal(models.Model):
	arboles = models.ForeignKey(Arboles)
	cantidad = models.FloatField()

	encuesta = models.ForeignKey(Encuesta)

	def __unicode__(self):
		return self.arboles.nombre

	class Meta:
		verbose_name = 'Inventario forestal'
		verbose_name_plural = 'Inventarios forestales'


class UsoInsumos(models.Model):
	nombre = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Insumo'
		verbose_name_plural = 'Insumos'

class InsumosUtilizados(models.Model):
    ''' opciones de manejo agroecologico
    '''
    uso = models.ForeignKey(UsoInsumos, verbose_name="Uso de opciones de manejo agroecologico")
    volumen = models.FloatField('Qué área, número o volumen')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.uso.nombre
    
    class Meta:
        verbose_name_plural = "Insumos Utilizados"

class ItemsFamiliar(models.Model):
	nombre = models.CharField(max_length=250)

	def __unicode__(self):
		return self.nombre

class EgresoFamiliar(models.Model):
	producto = models.ForeignKey(ItemsFamiliar)
	costo = models.FloatField()

	encuesta = models.ForeignKey(Encuesta)

	def __unicode__(self):
		return self.producto.nombre

	class Meta:
		verbose_name='Egreso familiar'
		verbose_name_plural = 'Egresos Familiares'