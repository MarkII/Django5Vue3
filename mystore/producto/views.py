from django.shortcuts import render

# Create your views here.

from producto.models import Categoria, Producto
from producto.serializers import CategoriaSerializer, ProductoSerializer
# from producto.permissions import IsAdminReadOnly

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django_filters.rest_framework import DjangoFilterBackend

class CategoriaModelViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class  = CategoriaSerializer
    permission_classes = []
    #lookup_field = 'slug' # Para buscar por el slug en vezz de por id
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['published']
    

class ProductoModelViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = []