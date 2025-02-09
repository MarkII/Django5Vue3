from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(null=True, blank=True, upload_to='img_productos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name="productos")
    
    def __str__(self):
        return self.nombre