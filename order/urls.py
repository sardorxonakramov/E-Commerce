from django.urls import path, include

from order.views.list_order import OrderListAPIView
from order.views.create_order import OrderCreateAPIView




urlpatterns = [
    path("", OrderListAPIView.as_view(), name="order-list"),
    path("create/", OrderCreateAPIView.as_view(), name="order-create"),
]
