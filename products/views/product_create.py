from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from products.models.product import Product
from products.serializers.product_create import ProductCreateSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [AllowAny]
