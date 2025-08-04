# Cart/services/total_price.py

from Cart.models.cart_item import CartItem

def get_cart_total_price(user):
    cart_items = CartItem.objects.filter(cart__user=user).select_related("product")
    total = sum(item.product.price * item.quantity for item in cart_items)
    return total
