from rest_framework.routers import DefaultRouter
from producto.views import CategoriaModelViewSet, ProductoModelViewSet

#Esto se hace para los modelviewsets

router_producto = DefaultRouter()

router_producto.register(prefix='categoria', basename='categoria', viewset=CategoriaModelViewSet)
router_producto.register(prefix='producto', basename='producto',  viewset=ProductoModelViewSet)