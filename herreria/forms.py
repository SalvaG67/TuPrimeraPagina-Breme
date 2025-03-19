from django import forms
from . import models

class PedidoForm(forms.ModelForm):
    class Meta:
        model = models.pedido
        fields = '__all__'