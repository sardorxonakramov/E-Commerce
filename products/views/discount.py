from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

from products.filters import DiscountFilter
from products.models import Discount
from products.serializers import (
    DiscountCreateSerializer,
    DiscountListSerializer,
    DiscountUpdateSerializer,
    DiscountDeleteSerializer,
)
from Common.permissions import allow_role



class DiscountListAPIView(generics.ListAPIView):
    queryset = Discount.objects.select_related("product").all()
    serializer_class = DiscountListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DiscountFilter
    search_fields = ["product__name"]
    ordering_fields = ["created_at", "expired_at", "percentage", "price"]
    permission_classes = [AllowAny]


class DiscountCreateAPIView(generics.CreateAPIView):


    queryset = Discount.objects.all()
    serializer_class = DiscountCreateSerializer
    permission_classes = [IsAuthenticated,allow_role.IsSeller]



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )


class DiscountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Discount.objects.select_related("product").all()
    serializer_class = DiscountListSerializer
    lookup_field = "id"
    permission_classes = [AllowAny]


class DiscountUpdateAPIView(generics.UpdateAPIView):


    queryset = Discount.objects.select_related("product").all()
    serializer_class = DiscountUpdateSerializer
    permission_classes = [IsAuthenticated,allow_role.IsSeller]


    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        # updated_by = self.request.user if hasattr(self.request, 'user') else None
        # serializer.save(updated_by=updated_by)
        serializer.save()


class DiscountDeleteAPIView(generics.DestroyAPIView):


    queryset = Discount.objects.all()
    serializer_class = DiscountDeleteSerializer
    permission_classes = [IsAuthenticated,allow_role.IsSeller]
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"detail": "Chegirma muvaffaqiyatli o‘chirildi."},
            status=status.HTTP_204_NO_CONTENT,
        )
