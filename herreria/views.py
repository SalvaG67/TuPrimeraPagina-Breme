from django.shortcuts import render, redirect
from .forms import PedidoForm
from .models import producto, pedido, cliente, vendedor
from django.http import HttpResponse

def productos_list(request):
    productos = producto.objects.all()
    return render(request, 'herreria/productos_list.html', {'productos': productos})
def pedidos_list(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos') 
    else:
        form = PedidoForm()

    pedidos = pedido.objects.all()  # Obtén los pedidos existentes
    return render(request, 'herreria/pedidos_list.html', {'pedidos': pedidos, 'form': form})
def inicio(request):
    return render(request, 'herreria/inicio.html')
def about(request):
    return render(request, 'herreria/about.html')

