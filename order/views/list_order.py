from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from order.models import Order
from order.serializers.order import OrderSerializer


class OrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user).prefetch_related('items', 'items__product')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
