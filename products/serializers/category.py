from rest_framework import serializers

from products.models.category import Category


class CategoryListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "image_url", "children")

    def get_image_url(self, obj):
        if obj.image and obj.image.file:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.file.url)
            return obj.image.file.url
        return None

    def get_children(self, obj):
        children = obj.children.all()
        return CategoryListSerializer(children, many=True, context=self.context).data


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "parent", "image")


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "parent", "image")


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = {"id"}
