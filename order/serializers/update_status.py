from rest_framework import serializers
from order.models.order import Order
from Common.choices.order import OrderStatus


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=OrderStatus.choices)

    class Meta:
        model = Order
        fields = ['status']
