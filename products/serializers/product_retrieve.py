from django.core.files.images import get_image_dimensions
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from products.models import Product
from products.models.image import ProductImage


class ProductImageField(serializers.Field):
    def to_representation(self, value):
        if value.exists():
            image = value.first().image
            if not image:
                return None
            return {
                "id": image.id,
                "url": image.image.url if image.image else None,
                "alt_text": image.alt_text or "",
                "width": image.width,
                "height": image.height,
            }
        return None


class ProductRetrieveSerializer(serializers.ModelSerializer):
    image = ProductImageField(source="images", read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "name",
            "description",
            "is_top",
            "stock",
            "price",
            "image",
        )
        read_only_fields = fields

    def get_image_url(self, obj):
        if obj.images.exists():
            image = obj.images.first().image
            request = self.context.get("request")
            if image and image.image:
                return request.build_absolute_uri(image.image.url) if request else image.image.url
        return None
