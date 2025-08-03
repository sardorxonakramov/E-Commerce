from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from Common.permissions.allow_role import RolePermission
from products.models.category import Category
from products.serializers.category import (
    CategoryCreateSerializer,
    CategoryListSerializer,
    CategoryUpdateSerializer,
    CategoryDeleteSerializer,
)


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Category.objects.filter(parent=None).prefetch_related("children")


class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny]


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = [AllowAny]
    # allowed_roles = ["Admin", "employee"]


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    permission_classes = [AllowAny]
    # allowed_roles = ["admin", "employee"]


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.first()
    serializer_class = CategoryDeleteSerializer
    permission_classes = [AllowAny]
    # allowed_roles = ["admin", "employee"]
