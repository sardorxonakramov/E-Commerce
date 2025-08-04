from django.db import models


class OrderItem(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)  # Yakuniy narx (chegirma qo‘llangan)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
