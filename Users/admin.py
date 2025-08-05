from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ("-id",)
    list_display = ("id", "phone", "email", "first_name", "last_name", "role", "is_active", "is_staff", "date_joined")
    list_filter = ("is_active", "is_staff", "is_superuser", "role")
    search_fields = ("phone", "email", "first_name", "last_name", "passport_series")
    readonly_fields = ("date_joined",)
    fieldsets = (
        (None, {"fields": ("phone", "email", "password")}),
        ("Shaxsiy ma'lumotlar", {"fields": ("first_name", "last_name", "passport_series")}),
        ("Ruxsatlar", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions", "role")}),
        ("Tizim ma'lumotlari", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "email", "password1", "password2", "role", "is_active", "is_staff", "is_superuser"),
        }),
    )
