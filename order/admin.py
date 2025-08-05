from django.contrib import admin
from order.models.order import Order
from order.models.item import OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_number', 'user_full_name', 'status', 'total_price', 'created_at']
    search_fields = ['order_number', 'user__first_name', 'user__last_name', 'user__phone']
    list_filter = ['status', 'created_at']
    readonly_fields = ['order_number', 'created_at', 'updated_at']
    ordering = ['-created_at']

    def user_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.phone
    user_full_name.short_description = "Buyurtmachi"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity', 'price']
    search_fields = ['order__order_number', 'product__name']
    list_filter = ['product']
