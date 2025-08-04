from rest_framework import serializers
from products.models.product import Product
from products.models.image import ProductImage
from products.models.upload import Upload


class ProductImageInputSerializer(serializers.Serializer):
    upload_id = serializers.IntegerField(write_only=True)
    is_main = serializers.BooleanField(default=False)

    def validate_upload_id(self, value):
        if not Upload.objects.filter(id=value).exists():
            raise serializers.ValidationError("Upload image not found.")
        return value



class ProductUpdateSerializer(serializers.ModelSerializer):
    images = ProductImageInputSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ["category", "name", "description", "price", "is_top", "stock", "images"]

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", None)

        # Asosiy maydonlarni yangilash
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Eski rasmlarni o‘chirib, yangilarini yozish
        if images_data is not None:
            instance.images.all().delete()
            for image_data in images_data:
                ProductImage.objects.create(
                    product=instance,
                    image_id=image_data["upload_id"],
                    is_main=image_data["is_main"]
                )

        return instance



# {
#   "name": {
#     "uz": "Yangilangan nom",
#     "ru": "Новое имя",
#     "en": "Updated Name"
#   },
#   "description": {
#     "uz": "Tavsif",
#     "ru": "Описание",
#     "en": "Description"
#   },
#   "price": "199000.00",
#   "stock": 7,
#   "is_top": true,
#   "images": [
#     {"upload_id": 12, "is_main": true},
#     {"upload_id": 14, "is_main": false}
#   ]
# }
