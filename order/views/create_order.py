from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from order.services.create_order import create_order_from_cart
from order.serializers.order import OrderSerializer


class OrderCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        address = request.data.get("address")

        if not address:
            return Response({"error": "Manzil (address) kiritilishi shart."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = create_order_from_cart(user=user, address=address)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
