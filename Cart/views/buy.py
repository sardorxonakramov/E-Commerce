from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from order.services.create_order import create_order_from_cart


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        address = request.data.get("address")
        if not address:
            return Response({"error": "Manzil (address) kiritilishi shart."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            order = create_order_from_cart(request.user, address)
            return Response({"message": "Buyurtma yaratildi", "order_id": order.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
