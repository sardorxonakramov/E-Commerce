# order/services/create_order.py

from django.db import transaction
from order.models.order import Order
from order.models.item import OrderItem
from Cart.models.cart_item import CartItem
from Cart.services.total_price import get_cart_total_price
from Common.generate_number import generate_order_number


@transaction.atomic
def create_order_from_cart(user):
    cart_items = CartItem.objects.filter(cart__user=user).select_related("product")

    if not cart_items.exists():
        raise Exception("Savat bo'sh")

    total_price = get_cart_total_price(user)

    order = Order.objects.create(
        user=user,
        total_price=total_price,
        order_number=generate_order_number(),
    )

    for item in cart_items:
        product = item.product

        # Mahsulot yetarli bo'lishini tekshiramiz
        if product.stock < item.quantity:
            raise Exception(f"{product.name} mahsulotdan yetarli emas")

        # Mahsulotdan chegiramiz
        product.stock -= item.quantity
        product.save()

        # OrderItem yaratamiz
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item.quantity,
            price=product.price
        )

    # Savatni tozalaymiz
    cart_items.delete()

    return order
