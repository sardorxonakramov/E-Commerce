from rest_framework.permissions import BasePermission
from Common.choices.role import RoleChoice


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == RoleChoice.ADMIN


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [ RoleChoice.EMPLOYEE, RoleChoice.ADMIN]


class IsDeliver(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [ RoleChoice.DELIVER, RoleChoice.ADMIN]


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [ RoleChoice.SELLER, RoleChoice.ADMIN]


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [ RoleChoice.USER, RoleChoice.ADMIN]

class IsEmployeeOrDeliver(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [RoleChoice.EMPLOYEE, RoleChoice.DELIVER, RoleChoice.ADMIN]
