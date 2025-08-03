from django.contrib import admin

from products.models.image import Upload


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    ...
