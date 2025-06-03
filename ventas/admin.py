from django.contrib import admin
from .models import Cliente, Venta, ItemVenta
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(ItemVenta)