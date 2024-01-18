from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),  # También mantén tu ruta existente para '/inicio/'
    path('productos', views.productos, name='productos'),
    path('soluciones', views.soluciones, name='soluciones'),
    path('precios', views.precios, name='precios'),
    path('conctacto', views.contacto, name='contacto'),
    path('confirmacion', views.confirmacion, name='confirmacion'),
]
