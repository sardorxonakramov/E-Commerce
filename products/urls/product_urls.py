from django.urls import path

from products.views import product_create, product_list  # ,ProductRetrieveView


urlpatterns = [
    path("create/", product_create.ProductCreateView.as_view(), name="product-create"),
    path("list/", product_list.ProductListView.as_view(), name="product-list"),
    # path("retrieve/<int:pk>", product_retrieve.ProductRetrieveView.as_view(), name="product-retrieve"),
]
