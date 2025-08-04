from rest_framework import serializers


class CartTotalPriceSerializer(serializers.Serializer):
    total_price = serializers.DecimalField(max_digits=12, decimal_places=2)
