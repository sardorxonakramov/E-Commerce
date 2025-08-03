from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User

    list_display = (
        "id", "phone", "email", "first_name", "last_name", "role",
        "is_active", "is_staff") #"created_at", "updated_at"
    # )
    list_filter = ("role", "is_active", "is_staff", "is_superuser")
    search_fields = ("phone", "email", "first_name", "last_name", "passport_series")
    ordering = ("-id",)

    readonly_fields = ("created_at", "updated_at", "created_by", "updated_by", "last_login")

    fieldsets = (
        (None, {"fields": ("phone", "email", "password")}),
        (_("Personal info"), {
            "fields": ("first_name", "last_name", "passport_series")
        }),
        (_("Permissions"), {
            "fields": (
                "role", "is_active", "is_staff", "is_superuser",
                "groups", "user_permissions"
            )
        }),
        (_("Important dates"), {
            "fields": ("last_login", "created_at", "updated_at", "created_by", "updated_by")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone", "email", "password1", "password2",
                "first_name", "last_name", "passport_series", "role",
                "is_active", "is_staff", "is_superuser"
            ),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")
