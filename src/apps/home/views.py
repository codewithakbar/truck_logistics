from rest_framework import viewsets

from apps.home.pagination import CustomPageNumberPagination
from .models import Products
from .serializers import ProductsSerializer
from .permissions import IsAdminOrDispatcherOrReadOnly


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminOrDispatcherOrReadOnly]
    pagination_class = CustomPageNumberPagination
