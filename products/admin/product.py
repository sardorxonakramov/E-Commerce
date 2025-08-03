from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from Common.admin import BaseAdmin
from products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    exclude = ("created_by", "updated_by")
    verbose_name = "Product Image"
    verbose_name_plural = "Product Images"


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    inlines = [ProductImageInline]
    list_display = ("id", "get_name_uz", "category", "price", "is_top", "stock")
    list_filter = ("category", "is_top")
    list_select_related = ("category",)
    search_fields = ("name",)
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
