# Cart/views/cart_total_price.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from Cart.serializers.cart_total_price import CartTotalPriceSerializer
from Cart.services.total_price import get_cart_total_price


class CartTotalPriceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total = get_cart_total_price(request.user)
        serializer = CartTotalPriceSerializer({"total_price": total})
        return Response(serializer.data)
