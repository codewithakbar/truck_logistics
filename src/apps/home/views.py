from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from .permissions import IsAdminOrDispatcher


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminOrDispatcher]

    