from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("created_by", "updated_by", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
