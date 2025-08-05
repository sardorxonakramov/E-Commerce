from django.utils import timezone
from rest_framework import serializers

from products.models import Discount


class DiscountListSerializer(serializers.ModelSerializer):

    product_name = serializers.SerializerMethodField()
    product_price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2, read_only=True)
    is_active = serializers.SerializerMethodField()
    days_remaining = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Discount
        fields = [
            "id",
            "product",
            "product_name",
            "product_price",
            "price",
            "percentage",
            "expired_at",
            "is_active",
            "days_remaining",
            "discounted_price",
        ]

    def get_product_name(self, obj):
        return obj.product.name

    def get_is_active(self, obj):
        return obj.expired_at > timezone.now()

    def get_days_remaining(self, obj):
        if obj.expired_at > timezone.now():
            return (obj.expired_at - timezone.now()).days
        return 0

    def get_discounted_price(self, obj):
        return float(obj.price) * (1 - obj.percentage / 100)


class BaseDiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ["product", "price", "percentage", "expired_at"]

    def validate_percentage(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Percentage must be between 0 and 100")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value

    def validate_expired_at(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Expiration date must be in the future")
        return value


class DiscountCreateSerializer(BaseDiscountSerializer):
    def validate(self, attrs):
        product = attrs.get("product")

        if Discount.objects.filter(product=product, expired_at__gt=timezone.now()).exists():
            raise serializers.ValidationError("An active discount already exists for this product")

        return attrs


class DiscountUpdateSerializer(BaseDiscountSerializer):

    def validate(self, attrs):
        instance = self.instance

        if instance.expired_at <= timezone.now():
            raise serializers.ValidationError("Cannot update expired discount")

        return attrs


class DiscountDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id')