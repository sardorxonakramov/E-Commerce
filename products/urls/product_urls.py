from django.urls import path

from products.views import product_create, product_list,product_crud # ,ProductRetrieveView


urlpatterns = [
    path("create/", product_create.ProductCreateView.as_view(), name="product-create"),
    path("", product_list.ProductListView.as_view(), name="product-list"),
    path('<int:pk>/update/', product_crud.ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', product_crud.ProductDeleteView.as_view(), name='product-delete'),

    # path("retrieve/<int:pk>", product_retrieve.ProductRetrieveView.as_view(), name="product-retrieve"),
]
