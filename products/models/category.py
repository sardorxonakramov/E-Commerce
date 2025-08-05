from django.db import models
from django.utils.translation import gettext_lazy as _  # noqa

from Common.models import BaseModel
from products.models.upload import Upload



class Category(BaseModel):

    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    image = models.ForeignKey(Upload, on_delete=models.CASCADE, null=True, blank=True, related_name="categories")

    class Meta:
        db_table = "categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["name"]
