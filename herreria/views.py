from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from .models import producto, pedido, cliente, vendedor
from django.http import HttpResponse

def productos_list(request):
    productos = producto.objects.all()
    return render(request, 'herreria/productos_list.html', {'productos': productos})
def pedidos_list(request):
    if request.method == 'POST':
        form = forms.PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos') 
    else:
        form = forms.PedidoForm()

    pedidos = pedido.objects.all()
    return render(request, 'herreria/pedidos_list.html', {'pedidos': pedidos, 'form': form})
def inicio(request):
    return render(request, 'herreria/inicio.html')
def about(request):
    return render(request, 'herreria/about.html')

def pedido_update(request, pk: int):
    query = pedido.objects.get(pk=pk)
    if request.method == 'GET':
        form = forms.PedidoForm(instance=query)
    if request.method == 'POST':
        form = forms.PedidoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
        else:
            print(form.errors)  
    return render(request, 'herreria/pedido_update.html', {'form': form})


def pedido_delete(request, pk: int):
    query = pedido.objects.get(pk=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('listar_pedidos')
    return render(request, 'herreria/pedido_confirm_delete.html', {'object': query})
