from rest_framework import serializers
from products.models.product import Product
from products.models.image import ProductImage
from products.models.upload import Upload


class ProductImageCreateSerializer(serializers.Serializer):
    image_id = serializers.PrimaryKeyRelatedField(queryset=Upload.objects.all())
    is_main = serializers.BooleanField(default=False)


class ProductCreateSerializer(serializers.ModelSerializer):
    images = ProductImageCreateSerializer(many=True, write_only=True)

    class Meta:
        model = Product
        fields = ["category", "name", "description", "price", "is_top", "stock", "images"]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        product = Product.objects.create(**validated_data)

        main_image_set = False
        for image_data in images_data:
            is_main = image_data.get("is_main", False)
            if is_main and not main_image_set:
                main_image_set = True
            elif is_main and main_image_set:
                is_main = False  #

            ProductImage.objects.create(
                product=product,
                image=image_data["image_id"],
                is_main=is_main
            )

        return product



