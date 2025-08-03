from django.db import models
from django.utils.translation import gettext_lazy as _  # noqa

from Common.models import BaseModel
from products.models.upload import Upload


class ProductImage(BaseModel):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="images")
    image = models.ForeignKey(
        Upload, on_delete=models.CASCADE, related_name="product_images", verbose_name="Image Upload"
    )
    is_main = models.BooleanField(default=False, verbose_name=_("Is Main Image"))

    class Meta:
        db_table = "product_images"
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
