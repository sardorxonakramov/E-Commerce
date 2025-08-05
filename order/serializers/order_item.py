from rest_framework import serializers
from order.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_id = serializers.IntegerField(source="product.id", read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "product_id",
            "product_name",
            "quantity",
            "price",
        ]
        read_only_fields = ["id", "product_id", "product_name", "price"]
