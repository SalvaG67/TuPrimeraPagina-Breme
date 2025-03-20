from django.contrib import admin
from .models import producto, pedido, cliente, vendedor

admin.site.register(pedido) 
admin.site.register(cliente)
admin.site.register(vendedor)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'descripcion', 'precio', 'stock')
    search_fields = ('nombre',)

admin.site.register(producto, ProductoAdmin)