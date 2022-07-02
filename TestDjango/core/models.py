from distutils.command.upload import upload
from django.db import models

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=50, verbose_name='descripcion')
    stock = models.IntegerField(verbose_name='Stock')
    precio = models.IntegerField(verbose_name='Precio')
    imagen = models.ImageField(upload_to='static/core/imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nombre
        
class Promocion(models.Model):
    idPromocion = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombrepro = models.CharField(max_length=100, verbose_name='Nombre')
    porcDesceunto = models.IntegerField(verbose_name='Porcentaje de descuento')
    precioFinal = models.IntegerField(verbose_name='Precio')
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombrepro
