from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoice(models.IntegerChoices):
    ADMIN = 0, _("Admin")
    EMPLOYEE = 1, _("Employee")
    DELIVER = 2, _("Delever")
    SELLER = 3, _("Seller")
    USER = 4, _("User")
