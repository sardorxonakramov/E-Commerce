from django.contrib import admin
from Cart.models.cart import Cart
from Cart.models.cart_item import CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('product_name',)
    fields = ('product', 'product_name', 'quantity')

    def product_name(self, obj):
        return obj.product.name
    product_name.short_description = 'Mahsulot nomi'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    search_fields = ('user__phone',)
    readonly_fields = ('created_at',)
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart_user', 'product_name', 'quantity')
    search_fields = ('cart__user__phone', 'product__name')
    list_select_related = ('cart', 'product')

    def cart_user(self, obj):
        return obj.cart.user.phone
    cart_user.short_description = 'Foydalanuvchi'

    def product_name(self, obj):
        return obj.product.name
    product_name.short_description = 'Mahsulot nomi'
