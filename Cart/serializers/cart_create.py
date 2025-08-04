from rest_framework import serializers
from Cart.models.cart_item import CartItem
from Cart.models.cart import Cart
from products.models.product import Product


class CartItemCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def validate(self, attrs):
        product_id = attrs["product_id"]
        quantity = attrs["quantity"]

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Bunday mahsulot mavjud emas.")

        self.product = product  # saqlab qo'yamiz create uchun

        user = self.context["request"].user
        cart, _ = Cart.objects.get_or_create(user=user)

        try:
            existing_item = CartItem.objects.get(cart=cart, product=product)
            total_quantity = existing_item.quantity + quantity
        except CartItem.DoesNotExist:
            total_quantity = quantity

        if total_quantity > product.stock:
            raise serializers.ValidationError(f"Jami miqdor {product.stock} dan oshmasligi kerak.")

        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        cart, _ = Cart.objects.get_or_create(user=user)
        product = self.product
        quantity = validated_data["quantity"]

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={"quantity": quantity},
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return cart_item
