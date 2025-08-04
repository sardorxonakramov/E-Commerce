from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from products.models.product import Product
from products.serializers.product_list import ProductListSerializer
from products.filters.product import ProductFilter
from Common.pagination import PageNumberPagination


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related("images", "discounts").all()
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price', 'name']
