from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("phone", "passport_series", "first_name", "last_name", "role")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("phone", "passport_series", "first_name", "last_name", "role", "is_active", "is_staff", "is_superuser")
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput,
        help_text="Kamida 8 ta belgidan iborat parol kiriting.",
    )
    password2 = forms.CharField(
        label="Parolni tasdiqlang",
        widget=forms.PasswordInput,
        help_text="Xuddi yuqoridagi parolni qayta kiriting.",
    )

    class Meta:
        model = User
        fields = ("phone", "email", "passport_series", "first_name", "last_name", "role")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "phone", "email", "passport_series",
            "first_name", "last_name", "role",
            "is_active", "is_staff", "is_superuser"
        )
