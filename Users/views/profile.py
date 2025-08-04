from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from Users.serializers.profile import (
    ProfileSerializers,
    ChangePasswordSerializer,
    UserSerializer,
)

User = get_user_model()


class UserDetailUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Faqat login bo‘lgan user o‘zini ko‘radi/tahrirlaydi
        return self.request.user


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)

        user.set_password(serializer.validated_data["new_password"])
        user.save()

        return Response(
            {"success": "Parol muvaffaqiyatli yangilandi"}, status=status.HTTP_200_OK
        )


from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, DestroyAPIView


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Hozircha


class UserDetailView(RetrieveUpdateAPIView):
    """Admin uchun update"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
