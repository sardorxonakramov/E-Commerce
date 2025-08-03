from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    """Foydalanuvchi roli asosida ruxsat beradi """

    def has_permission(self, request, view):
        user = request.user
        allowed_roles = getattr(view, 'allowed_roles', [])

        return user.is_authenticated and user.role in allowed_roles


"""
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import RolePermission

class SomeProtectedView(APIView):
    permission_classes = [RolePermission]
    allowed_roles = ['admin', 'seller']  # faqat admin va seller ko‘ra oladi

    def get(self, request):
        return Response({"message": "Welcome authorized user!"})

"""