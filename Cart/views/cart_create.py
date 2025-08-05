from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from Cart.serializers.cart_create import CartItemCreateSerializer


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CartItemCreateSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            cart_item = serializer.save()
            return Response({"message": "Mahsulot savatga qo‘shildi."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {
#   "product_id": 3,
#   "quantity": 3
# }
