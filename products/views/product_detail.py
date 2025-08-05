from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from products.models.product import Product
from products.serializers.product_detail import ProductDetailSerializer


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductDetailSerializer(product, context={"request": request})
        return Response(serializer.data)
