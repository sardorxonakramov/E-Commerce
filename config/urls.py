from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views import defaults as default_views
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", include("rest_framework.urls")),  # web sahifada api test qilish uchun login

    path("api/auth/", include("Users.urls.auth"), name="Auth"),
    path("api/profile/", include("Users.urls.profile"), name="Profile"),
    
    path('api/',include('products.endpoints'), name = 'products'),
    path('api/cart/',include('Cart.urls'), name = 'Cart'),
    path('api/orders/',include('order.urls'),name='order')
]
# docs
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += [
        path("400/", default_views.bad_request, kwargs={"exception": Exception("Bad Request!")}),
        path("403/", default_views.permission_denied, kwargs={"exception": Exception("Permission Denied!")}),
        path("404/", default_views.page_not_found, kwargs={"exception": Exception("Page not Found!")}),
        path("500/", default_views.server_error),
    ]

if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )




