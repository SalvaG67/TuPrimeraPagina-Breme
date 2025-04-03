from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PedidoForm(forms.ModelForm):
    class Meta:
        model = models.pedido
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.producto
        fields = '__all__'

from django.contrib.auth.forms import AuthenticationForm

class loginForm(AuthenticationForm):
    class meta:
        model = AuthenticationForm
        fields = ['username', 'password']

class registerForm(UserCreationForm):
    class meta:
        model = User 
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Contraseña'
        self.fields['password2'].help_text = 'Confirmar Contraseña'