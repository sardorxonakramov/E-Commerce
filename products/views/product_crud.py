from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from products.models.product import Product
from products.serializers.product_crud import ProductUpdateSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [AllowAny]
    lookup_field = "pk"


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "pk"
