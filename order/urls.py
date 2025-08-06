from django.urls import path, include

from order.views.list_order import OrderListAPIView
from order.views.create_order import OrderCreateAPIView
from order.views.update_status import OrderStatusUpdateAPIView




urlpatterns = [
    path("", OrderListAPIView.as_view(), name="order-list"),
    path("create/", OrderCreateAPIView.as_view(), name="order-create"),
    path('<int:pk>/status/', OrderStatusUpdateAPIView.as_view(), name='order-update-status'),

]

# ---------------- buy ni o'z ichiga oladi ------------
# {
#     "address":"Toshkent"
# }
# buyurtma holatini o'zgartirishda shuni kirtsa bas
# {
# "status":2
# }