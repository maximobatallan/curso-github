from django.contrib import admin
from .models import Categoria, MovimientoStock, Producto
# Register your models here.
admin.site.register(Categoria)
admin.site.register(MovimientoStock)
admin.site.register(Producto)