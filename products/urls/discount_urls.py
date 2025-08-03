from django.urls import path

from products.views import (
    DiscountCreateAPIView,
    DiscountListAPIView,
    DiscountRetrieveAPIView,
    DiscountUpdateAPIView,
)

urlpatterns = [
    path("", DiscountListAPIView.as_view(), name="discount-list"),
    path("create/", DiscountCreateAPIView.as_view(), name="discount-create"),
    path("<int:id>/", DiscountRetrieveAPIView.as_view(), name="discount-retrieve"),
    path("<int:id>/update/", DiscountUpdateAPIView.as_view(), name="discount-update"),
]
