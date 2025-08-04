# order/views/create_order.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from order.services.create_order import create_order_from_cart


class OrderCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            order = create_order_from_cart(user)
            return Response({"message": "Buyurtma muvaffaqiyatli yaratildi", "order_id": order.id})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
