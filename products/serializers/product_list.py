
from rest_framework import serializers
from products.models.product import Product
from products.models.image import ProductImage
from products.models.discount import Discount


class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'discount']

    def get_image(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        if main_image and main_image.image and main_image.image.file:
            return main_image.image.file.url
        return None

    def get_discount(self, obj):
        discount = obj.discounts.order_by("-created_at").first()
        if discount:
            return {
                "price": discount.price,
                "percentage": discount.percentage,
                "expired_at": discount.expired_at
            }
        return None
