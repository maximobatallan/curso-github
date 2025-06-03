from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('productos/', views.productos_disponibles, name='productos_disponibles'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
