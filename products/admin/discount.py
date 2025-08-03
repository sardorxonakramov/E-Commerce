from django.contrib import admin

from products.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "price", "percentage", "expired_at", "created_at")
    list_filter = ("product", "expired_at")
    search_fields = ("product__name",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
