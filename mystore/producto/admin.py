from django.contrib import admin
from producto.models import Producto, Categoria


# Register your models here.

@admin.register(Categoria)
class CategoriaAdminPanel(admin.ModelAdmin):
    model = Categoria
    field = '__all__'

@admin.register(Producto)
class ProductoAdminPanel(admin.ModelAdmin):
    model = Producto
    field = '__all__'