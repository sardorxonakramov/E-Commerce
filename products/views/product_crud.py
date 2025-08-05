from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from products.models.product import Product
from products.serializers.product_crud import ProductUpdateSerializer
from Common.permissions import allow_role


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated,allow_role.IsSeller]
    lookup_field = "pk"


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated,allow_role.IsSeller]
    lookup_field = "pk"
