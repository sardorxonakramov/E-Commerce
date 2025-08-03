from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from Common.permissions.allow_role import RolePermission
from products.filters import DiscountFilter
from products.models import Discount
from products.serializers import (
    DiscountCreateSerializer,
    DiscountListSerializer,
    DiscountUpdateSerializer,
)


class DiscountListAPIView(generics.ListAPIView):
    queryset = Discount.objects.select_related("product").all()
    serializer_class = DiscountListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DiscountFilter
    search_fields = [
        "product__name",
    ]
    ordering_fields = ["created_at", "expired_at", "percentage", "price"]


class DiscountCreateAPIView(generics.CreateAPIView):
    """API View for creating discounts"""

    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes =[AllowAny]
    # permission_classes = [RolePermission]
    # allowed_roles =['admin','employee','seller']


class DiscountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Discount.objects.select_related("product").all()
    serializer_class = DiscountListSerializer
    lookup_field = "id"


class DiscountUpdateAPIView(generics.UpdateAPIView):
    """API View for updating discounts (PUT and PATCH)"""

    queryset = Discount.objects.select_related("product").all()
    serializer_class = DiscountUpdateSerializer
    permission_classes = [RolePermission]
    allowed_roles =['admin','employee','seller']

    lookup_field = "id"

    def perform_update(self, serializer):
        serializer.save(updated_by == self.request.user)
