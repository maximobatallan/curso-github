from django.shortcuts import render, redirect,get_object_or_404
from .models import Cliente, Venta, ItemVenta
from .forms import ClienteForm, ItemVentaForm
from django.utils import timezone

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:listado_cliente')
    else:
        form = ClienteForm()
    return render(request, 'ventas/formulario_cliente.html', {'form': form} )

def listado_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/listado_clientes.html', {'clientes': clientes})

def crear_venta(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ItemVentaForm(request.POST)
        if form.is_valid():
            venta = Venta.objects.create(cliente=cliente, fecha=timezone.now())
            item = form.save(commit=False)
            item.venta = venta
            item.save()
            return redirect('ventas:listado_ventas')
    else:
        form= ItemVentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form, 'cliente':cliente} )

def listado_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listado_ventas.html', {'ventas': ventas})