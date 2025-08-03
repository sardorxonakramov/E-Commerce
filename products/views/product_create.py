from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from Common.permissions.allow_role import RolePermission
from products.serializers import ProductCreateSerializer

# from products.services.product import ProductService


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    # service_class = ProductService
    permission_classes = [AllowAny]
    # allowed_roles = ["admin", "seller"]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # product = self.service_class.create_product(
        #     request.user.id, serializer.validated_data
        # )
        return Response(
            self.get_serializer(product).data, status=status.HTTP_201_CREATED
        )
