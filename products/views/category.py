from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from products.models.category import Category
from products.serializers.category import (
    CategoryCreateSerializer,
    CategoryListSerializer,
    CategoryUpdateSerializer,
    CategoryDeleteSerializer,
)
from Common.permissions import allow_role


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
    permission_classes = [IsAuthenticated, allow_role.IsEmployee]


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    permission_classes = [IsAuthenticated, allow_role.IsEmployee]


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer
    permission_classes = [IsAuthenticated, allow_role.IsAdmin]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        children_count = instance.children.count()
        if children_count:
            print(f"{children_count} ta bolalar kategoriyasi ham o‘chiriladi.")

        self.perform_destroy(instance)
        return Response(
            {
                "detail": f"Kategoriya va unga tegishli {children_count} ta bola kategoriya o‘chirildi."
            },
            status=status.HTTP_204_NO_CONTENT,
        )

    def perform_destroy(self, instance):

        for child in instance.children.all():
            child.delete()
        instance.delete()
