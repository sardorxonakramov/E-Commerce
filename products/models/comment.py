from django.db import models
from django.utils.translation import gettext_lazy as _  # noqa

#
from Common.models import BaseModel


#
#
class Comment(BaseModel):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="comments")
    full_name = models.CharField(max_length=255)  # visitor name
    rate = models.IntegerField()  # 1–5 stars
    comment = models.TextField()

    class Meta:
        db_table = "comments"
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["-created_at"]
