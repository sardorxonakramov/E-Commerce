from django.urls import path

from Users.views.profile import (
    UserDetailUpdateView,
    ChangePasswordView,
    UserListView,
    UserDetailView,
    UserDeleteView,
)


urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("me/", UserDetailUpdateView.as_view(), name="update"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"), # employe uchun
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"), 
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
