from rest_framework import viewsets, status
from rest_framework.response import Response

from django.db.models import Q

from apps.home.pagination import CustomPageNumberPagination
from .models import Products
from .serializers import ProductsSerializer
from .permissions import IsAdminOrDispatcherOrReadOnly



class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminOrDispatcherOrReadOnly]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get("s", None)
        if search_query:
            queryset = queryset.filter(
                Q(olib_ketish__icontains=search_query)
                | Q(tashlab_ketish__icontains=search_query)
                | Q(yuk_turi__icontains=search_query)
                | Q(phone__icontains=search_query)
                | Q(email__icontains=search_query)
            )
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        recommendations = Products.objects.filter(
            Q(transport_turi=instance.transport_turi)
            | Q(olib_ketish=instance.olib_ketish)
            | Q(tashlab_ketish=instance.tashlab_ketish)
        ).exclude(id=instance.id)[:5]

        recommendations_serializer = self.get_serializer(recommendations, many=True)

        data = {
            "product": serializer.data,
            "recommendations": recommendations_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
