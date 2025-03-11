from django.shortcuts import render
from .models import producto, pedido, cliente, vendedor
from django.http import HttpResponse

def listar_productos(request):
    productos = producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

# Create your views here.
