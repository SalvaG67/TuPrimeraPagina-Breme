from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class pedido (models.Model):
    cliente = models.ForeignKey('herreria.cliente', on_delete=models.CASCADE)
    vendedor = models.ForeignKey('herreria.vendedor', on_delete=models.CASCADE)
    productos = models.ManyToManyField('herreria.producto')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()

    def __str__(self):
        return f"pedido de {self.cliente.nombre}"

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.nombre
    
class vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre