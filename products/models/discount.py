from django.db import models
from django.utils.translation import gettext_lazy as _  # noqa

#
from Common.models import BaseModel


#
#
class Discount(BaseModel):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="discounts")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.IntegerField()  # e.g. 20 means 20% off
    expired_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "discounts"
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")
        ordering = ["-created_at"]
