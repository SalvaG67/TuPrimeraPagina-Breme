from django.contrib import admin
from .models import producto, pedido, cliente, vendedor

admin.site.register(producto)
admin.site.register(pedido) 
admin.site.register(cliente)
admin.site.register(vendedor)
# Register your models here.
