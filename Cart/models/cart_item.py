from django.db import models

class CartItem(models.Model):
    cart = models.ForeignKey(
        'Cart.Cart',
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')  # bitta mahsulot cartda faqat 1 marta bo'ladi

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
