from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from Common.admin import BaseAdmin
from products.models.category import Category


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ("id", "parent")
    search_fields = ("name",)
    list_filter = ("parent",)
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
