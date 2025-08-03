from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        "Users.User",
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        "Users.User",
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RoleChoice(models.IntegerChoices):
    ADMIN = 0, _("Admin")
    EMPLOYEE = 1, _("Employee")
    DELIVER = 2, _("Delever")
    SELLER = 3, _("Seller")
    USER = 4, _("User")
