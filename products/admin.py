from django.contrib import admin

from products.models.product import Product
from products.models.category import Category
from products.models.image import ProductImage
from products.models.comment import Comment
from products.models.discount import Discount
from products.models.upload import Upload


# ========== Inline'lar ==========

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    readonly_fields = ['is_main']


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    readonly_fields = ['full_name', 'rate', 'comment', 'created_at']
    can_delete = False


class DiscountInline(admin.TabularInline):
    model = Discount
    extra = 0


# ========== Model Adminlari ==========

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'is_top', 'get_category_name')
    search_fields = ('name',)
    list_filter = ('is_top', 'category')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProductImageInline, CommentInline, DiscountInline]

    def get_category_name(self, obj):
        return obj.category.name if obj.category else "-"
    get_category_name.short_description = "Kategoriya"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_parent_name')
    search_fields = ('name',)
    list_filter = ('parent',)
    readonly_fields = ('created_at', 'updated_at')

    def get_parent_name(self, obj):
        return obj.parent.name if obj.parent else "-"
    get_parent_name.short_description = "Ota Kategoriya"


# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product', 'image', 'is_main')
#     list_filter = ('is_main', 'product')
#     readonly_fields = ('created_at', 'updated_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_product_name', 'full_name', 'rate', 'created_at')
    search_fields = ('full_name', 'comment')
    list_filter = ('rate',)
    readonly_fields = ('created_at', 'updated_at')

    def get_product_name(self, obj):
        return obj.product.name
    get_product_name.short_description = "Mahsulot"


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_product_name', 'price', 'percentage', 'expired_at')
    list_filter = ('expired_at',)
    readonly_fields = ('created_at', 'updated_at')

    def get_product_name(self, obj):
        return obj.product.name
    get_product_name.short_description = "Mahsulot"


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'quality')
    list_filter = ('quality',)
