from rest_framework import serializers


class ProductImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image_url = serializers.SerializerMethodField()
    is_main = serializers.BooleanField()

    def get_image_url(self, obj):
        if obj.image and obj.image.file:
            return self.context['request'].build_absolute_uri(obj.image.file.url)
        return None
