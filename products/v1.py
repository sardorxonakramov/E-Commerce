from django.urls import include, path

urlpatterns = [
    path(
        "category/",
        include(("products.urls.category_url", "category"), namespace="category"),
    ),
    path(
        "product/",
        include(("products.urls.product_urls", "product"), namespace="product"),
    ),
    path(
        "upload/",
        include(("products.urls.upload_url", "upload"), namespace="upload"),
    ),
    path(
        "discount/",
        include(("products.urls.discount_urls", "discount"), namespace="discount"),
    ),
]
