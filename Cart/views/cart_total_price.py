from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from Cart.models.cart_item import CartItem
from Cart.serializers.cart_total_price import CartTotalPriceSerializer


class CartTotalPriceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(cart__user=user).select_related("product")

        total = sum(
            item.product.price * item.quantity for item in cart_items
        )

        serializer = CartTotalPriceSerializer({"total_price": total})
        return Response(serializer.data)
