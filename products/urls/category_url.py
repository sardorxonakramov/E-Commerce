from django.urls import path

from products.views.category import (
    CategoryCreateView,
    CategoryListView,
    CategoryRetrieveView,
    CategoryUpdateView,
)

urlpatterns = [
    path("", CategoryListView.as_view(), name="category-list"),
    path(
        "<int:pk>/", CategoryRetrieveView.as_view(), name="category-retrieve"
    ),
    path("create/", CategoryCreateView.as_view(), name="category-create"),
    path(
        "<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "<int:pk>/delete/",
        CategoryUpdateView.as_view(),
        name="category-delete",
    ),
]
