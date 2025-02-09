from rest_framework.serializers import ModelSerializer
from producto.models import  Categoria, Producto

class CategoriaSerializer(ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']
        

class ProductoSerializer(ModelSerializer):
    
    categoria = CategoriaSerializer
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen', 'categoria']