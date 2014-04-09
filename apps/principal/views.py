from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Articulo,Cliente,Unidad

class ArticuloList(ListView):
	template_name = "articulo/articulo_lista.html"
	model = Articulo
	context_object_name = 'Articulos'

class ArticuloNuevo(CreateView):
	template_name = "articulo/articulo_nuevo.html"
	model = Articulo
	success_url = "/listarticulo"

class ClienteList(ListView):
	template_name ="cliente/cliente_lista.html"
	model = Cliente
	context_object_name = 'Clientes'

class ClienteNuevo(CreateView):
	template_name = "cliente/cliente_nuevo.html"
	model = Cliente 
	success_url = "/listaclientes"

class UnidadList(ListView):
	template_name = "unidad/unidad_lista.html"
	model = Unidad
	context_object_name = "Unidades"

class UnidadNueva(CreateView):
	template_name = "unidad/unidad_nueva.html"
	model = Unidad
	success_url = "/listaunidad"



