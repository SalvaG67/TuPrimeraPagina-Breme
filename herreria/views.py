from django.shortcuts import render
from .models import producto, pedido, cliente, vendedor
from django.http import HttpResponse

def listar_productos(request):
    productos = producto.objects.all()
    return render(request, 'herreira/listar_productos.html', {'productos': productos})
def listar_pedidos(request):
    pedidos = pedido.objects.all()    
    return render(request, 'herreria/listar_pedidos.html', {'pedidos': pedidos})
# Create your views here.
def inicio(request):
    return render(request, 'herreria/inicio.html')
def about(request):
    return render(request, 'herreria/about.html')
