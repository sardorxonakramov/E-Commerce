from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from products.models.product import Product
from products.serializers.product_create import ProductCreateSerializer
from Common.permissions import allow_role


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated,allow_role.IsSeller]
