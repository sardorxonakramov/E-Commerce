from django.urls import include, path

urlpatterns = [
    path(
        "categories/",
        include(("products.urls.category_url", "category"), namespace="category"),
    ),
    path(
        "products/",
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
    path(
        "comment/",
        include(("products.urls.comment_urls", "comment"), namespace="comment"),
    ),
]
