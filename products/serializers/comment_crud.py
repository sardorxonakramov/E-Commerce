from rest_framework import serializers
from products.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "product", "full_name", "rate", "comment", "created_at"]
        read_only_fields = ["created_at"]
