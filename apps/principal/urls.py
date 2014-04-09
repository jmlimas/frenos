from django.conf.urls import patterns, include, url

from apps.principal.views import ArticuloList
from apps.principal.views import ArticuloNuevo
from apps.principal.views import ClienteList
from apps.principal.views import ClienteNuevo
from apps.principal.views import UnidadList,UnidadNueva

urlpatterns = patterns('apps.principal.views',
	url(r'^listarticulo/',ArticuloList.as_view(),name='lista_articulo'),
	url(r'^nuevoarticulo/',ArticuloNuevo.as_view(),name='nuevo_articulo'),
	url(r'^listaclientes/',ClienteList.as_view(),name= 'lista_cliente'),
	url(r'^nuevocliente/',ClienteNuevo.as_view(),name='nuevo_cliente'),
	url(r'^listaunidad/',UnidadList.as_view(),name='lista_unidad'),
	url(r'^nuevaunidad/',UnidadNueva.as_view(),name='nueva_unidad'),

)
