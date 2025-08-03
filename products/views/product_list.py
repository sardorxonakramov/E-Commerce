from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from products.filters import ProductFilter
from products.models import Product
from products.serializers import ProductListSerializer,ProductImagesSerializer


class ProductListView(ListAPIView):
    """
    API view to list all products.
    """

    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ["name__uz", "description__uz"]
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.all().order_by("?").prefetch_related("images__image")
