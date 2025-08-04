from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from Cart.models.cart_item import CartItem
from Cart.serializers.cart_crud import CartItemUpdateSerializer


class CartItemUpdateView(UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        item = super().get_object()
        if item.cart.user != self.request.user:
            raise ValidationError("You do not have permission to update this item.")
        return item

    def perform_update(self, serializer):
        item = self.get_object()
        product = item.product
        new_quantity = serializer.validated_data["quantity"]

        if product.stock < new_quantity:
            raise ValidationError("Not enough stock available.")

        serializer.save()


class CartItemDeleteView(DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        item = super().get_object()
        if item.cart.user != self.request.user:
            raise ValidationError("You do not have permission to delete this item.")
        return item
