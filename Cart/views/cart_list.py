from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Cart.models.cart import Cart
from Cart.models.cart_item import CartItem
from Cart.serializers.cart_list import CartItemListSerializer


class CartDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        items = CartItem.objects.filter(cart=cart).select_related("product")
        serializer = CartItemListSerializer(items, many=True, context={"request": request})
        # serializer = CartItemListSerializer(items, many=True)

        return Response(serializer.data)
