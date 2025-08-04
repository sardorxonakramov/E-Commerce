from django.urls import path
from Cart.views.cart_create import AddToCartView
from Cart.views.cart_list import CartDetailAPIView
from Cart.views.cart_crud import CartItemUpdateView, CartItemDeleteView
from Cart.views.cart_total_price import CartTotalPriceView
from Cart.views.buy import CreateOrderView

urlpatterns = [
    path("add/", AddToCartView.as_view(), name="add-to-cart"),
    path("cart/", CartDetailAPIView.as_view(), name="cart-detail"),

    path("cart/item/<int:pk>/update/", CartItemUpdateView.as_view(), name="cart-item-update"),
    path("cart/item/<int:pk>/delete/", CartItemDeleteView.as_view(), name="cart-item-delete"),
    path("total/", CartTotalPriceView.as_view(), name="cart-total-price"),
    path('buy/', CreateOrderView.as_view(), name='cart-buy'),
]

