from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatus(models.TextChoices):
    PROCESSING = '0', _('Jarayonda')
    SHIPPED = '1', _('Jo‘natilgan')
    DELIVERED = '2', _('Yetkazilgan')
