from rest_framework import serializers
from order.models import Order
from order.serializers.order_item import OrderItemSerializer


class UserSummarySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.SerializerMethodField()
    phone = serializers.CharField()
    email = serializers.EmailField()

    def get_full_name(self, obj):
        return f"{obj.first_name or ''} {obj.last_name or ''}".strip()


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = UserSummarySerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'status',
            'total_price',
            'created_at',
            'address',
            'user',
            'items',
        ]
