from django.utils import timezone
from rest_framework import serializers

from products.models import Product

from .discount import DiscountListSerializer


class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source="images.first.image.image", read_only=True)
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "price", "image", "discount")

    def get_discount(self, obj):
        discount = obj.discounts.filter(expired_at__gt=timezone.now()).first()
        if discount:
            return {"price": discount.price, "percentage": discount.percentage, "expired_at": discount.expired_at}
        return None
