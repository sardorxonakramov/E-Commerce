from rest_framework import viewsets, mixins, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from order.models import Order
from order.serializers import (
    OrderListSerializer,
    OrderDetailSerializer,
    OrderStatusUpdateSerializer,
)


class OrderViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):

    queryset = (
        Order.objects.select_related("user").prefetch_related("items__product").all()
    )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]
    permission_classes = [permissions.AllowAny]  # Keyin RoleBased ga o‘zgartirasan

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer
        elif self.action == "retrieve":
            return OrderDetailSerializer
        elif self.action == "partial_update":
            return OrderStatusUpdateSerializer
        return OrderListSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Order status updated successfully"}, status=status.HTTP_200_OK
        )
