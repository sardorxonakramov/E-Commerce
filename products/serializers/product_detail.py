from rest_framework import serializers

from products.models.product import Product
from products.models.discount import Discount
from products.models.image import ProductImage
from products.models.comment import Comment
from products.serializers.product_image import ProductImageSerializer
from products.serializers.comment import CommentSerializer


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()
    average_rate = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id", "name", "description", "price", "discounted_price", "stock", "is_top",
            "images", "comments", "average_rate", "category"
        )

    def get_images(self, obj):
        images = obj.images.all()
        return ProductImageSerializer(images, many=True, context=self.context).data

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializer(comments, many=True).data

    def get_discounted_price(self, obj):
        discount = obj.discounts.filter(expired_at__isnull=True).order_by('-created_at').first()
        if discount:
            return str(discount.price)
        return None

    def get_average_rate(self, obj):
        comments = obj.comments.all()
        if not comments.exists():
            return None
        total = sum(c.rate for c in comments)
        return round(total / comments.count(), 1)
