# from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from products.models import Product
from products.models.image import ProductImage


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]
        read_only_fields = ["id"]


# @extend_schema_serializer(
#     examples=[
#         OpenApiExample(
#             name="Product Create Example",
#             value={
#                 "name": {"en": "Phone", "ru": "Телефон", "uz": "Telefon"},
#                 "description": {"en": "Smartphone", "ru": "Смартфон", "uz": "Smartfon"},
#                 "category": 1,
#                 "price": 199.99,
#                 "is_top": True,
#                 "stock": 20,
#                 "images": [{"image": 1}],
#                 "banners": [{"image": 1}],
#             },
#         )
#     ]
# )
class ProductCreateSerializer(serializers.ModelSerializer):
    name = serializers.JSONField(default=dict)
    description = serializers.JSONField(default=dict)
    # banners = BannerCreateSerializer(many=True, required=False)
    images = ProductImagesSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "description",
            "price",
            "is_top",
            "stock",
            "images",
        ]
