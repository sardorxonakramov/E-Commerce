from django.urls import path

from Users.views.profile import UserDetailUpdateView, ChangePasswordView


urlpatterns = [
    path("me/", UserDetailUpdateView.as_view(), name="update"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
