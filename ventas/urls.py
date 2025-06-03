from django.urls import path
from . import views

app_name ='ventas'

urlpatterns = [
    path('clientes/', views.listado_clientes, name='listado_cliente'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('crear/<int:cliente_id>/', views.crear_venta, name='crear_venta'),
    path('', views.listado_ventas, name='listado_ventas')
    
]
