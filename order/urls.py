from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views.order import OrderViewSet
from order.views.create_order import OrderCreateAPIView


router = DefaultRouter()
router.register('orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
        path("create/", OrderCreateAPIView.as_view(), name="order-create"),

]
