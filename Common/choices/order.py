from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatus(models.TextChoices):
    PROCESSING = 'processing', _('Jarayonda')
    SHIPPED = 'shipped', _('Jo‘natilgan')
    DELIVERED = 'delivered', _('Yetkazilgan')
