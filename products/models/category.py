from django.db import models
from django.utils.translation import gettext_lazy as _  # noqa

from Common.models import BaseModel
from products.models.upload import Upload
from Common.utils import default_translation  



class Category(BaseModel):
    name = models.JSONField(
        default=default_translation
    )
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    image = models.ForeignKey(Upload, on_delete=models.CASCADE, null=True, blank=True, related_name="categories")

    class Meta:
        db_table = "categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["name"]
