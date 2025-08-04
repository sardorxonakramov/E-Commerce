import random
from django.db import models
from django.utils.translation import gettext_lazy as _
from Common.models import BaseModel
from Common.choices.order import OrderStatus


def generate_order_number():
    return str(random.randint(10**6, 10**7 - 1))  # 7 xonali noyob raqam


class Order(BaseModel):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=7, unique=True, default=generate_order_number, editable=False)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PROCESSING)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.order_number} - {self.user.get_full_name() or self.user.email}"
