from django import forms
from . import models

class PedidoForm(forms.ModelForm):
    class Meta:
        model = models.pedido
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.producto
        fields = '__all__'