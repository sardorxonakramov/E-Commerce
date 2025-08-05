from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from order.models.order import Order
from order.serializers.update_status import OrderStatusUpdateSerializer
from Common.permissions.allow_role import IsEmployeeOrDeliver


class OrderStatusUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsEmployeeOrDeliver]

    def patch(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"detail": "Buyurtma topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "detail": "Buyurtma holati yangilandi",
            "status": serializer.data['status']
        }, status=status.HTTP_200_OK)
