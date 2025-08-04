from rest_framework import serializers
from Cart.models.cart_item import CartItem
from products.models.product import Product
from products.models.image import ProductImage


class CartProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "price", "stock", "image_url")

    def get_image_url(self, obj):
        image = ProductImage.objects.filter(product=obj, is_main=True).first()
        request = self.context.get("request")
        if image and image.image and request:
            return request.build_absolute_uri(image.image.url)
        return None


class CartItemListSerializer(serializers.ModelSerializer):
    product = CartProductSerializer()

    class Meta:
        model = CartItem
        fields = ("id", "product", "quantity")
