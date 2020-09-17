from rest_framework import viewsets
from app.models import Productos
from app.serializer import ProductosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
