from django.db import models
from apps.principal.models import Cliente
from apps.principal.models import Unidad
from apps.principal.models import Articulo 

# Create your models here.
class Servicio(models.Model):
	cliente    = models.ForeignKey(Cliente)
	unidad     = models.ForeignKey(Unidad)
	articulo   = models.ForeignKey(Articulo)	
	km         = models.IntegerField()
	nextvisita = models.DateTimeField(auto_now=True)    
	created    = models.DateTimeField(auto_now_add=True)
	updated    = models.DateTimeField(auto_now=True)
    


