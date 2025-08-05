from django.db import transaction
from order.models.order import Order
from order.models.item import OrderItem
from Cart.models.cart_item import CartItem
from Cart.services.total_price import get_cart_total_price
from Common.generate_number import generate_order_number


@transaction.atomic
def create_order_from_cart(user, address: str):
    cart_items = CartItem.objects.filter(cart__user=user).select_related("product")

    if not cart_items.exists():
        raise Exception("Savat bo'sh")

    total_price = get_cart_total_price(user)

    order = Order.objects.create(
        user=user,
        total_price=total_price,
        order_number=generate_order_number(),
        address=address  # yangi manzil tashqaridan olinadi
    )

    for item in cart_items:
        product = item.product

        if product.stock < item.quantity:
            raise Exception(f"{product.name} mahsulotdan yetarli emas")

        product.stock -= item.quantity
        product.save()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item.quantity,
            price=product.price
        )

    cart_items.delete()

    return order
