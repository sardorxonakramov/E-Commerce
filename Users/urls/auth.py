# Users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from Users.views.auth import CustomTokenObtainPairView, RegisterView

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="custom_login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
]
