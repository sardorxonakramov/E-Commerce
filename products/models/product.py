from django.db import models
from django.utils.translation import gettext_lazy as _  # noqa

from Common.models import BaseModel
from Common.utils import default_translation  


class Product(BaseModel):
    category = models.ForeignKey(
        "products.Category",
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )
    name = models.JSONField(
        default=default_translation
    )
    description = models.JSONField(
        default=default_translation
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_top = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.id}"

    @property
    def get_name_uz(self):
        return self.name.get("uz", "No Name")

    class Meta:
        db_table = "products"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["-is_top", "name"]
