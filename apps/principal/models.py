from django.db import models

# Create your models here.

class Articulo(models.Model):
	clave = models.CharField(max_length=6, unique=True)
	nombre = models.CharField(max_length=180)
	precio = models.DecimalField(max_digits=19, decimal_places=2)
	img    = models.ImageField(upload_to='media/', blank=True, null=True)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return  self.nombre


class Cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	correo = models.EmailField(max_length=80,blank=True,null=True)
	telefono = models.CharField(max_length=14, blank= True,null=True)
	celular = models.CharField(max_length=10, blank=True, null=True)	
	status = models.BooleanField(default=True)


	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
		return nombreCompleto
		
		
class Unidad(models.Model):
	marca = models.CharField(max_length=140)
	modelo = models.CharField(max_length=140)
	ano = models.IntegerField()
	placas = models.CharField(max_length=8,blank=True, null=True)
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.marca





