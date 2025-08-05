from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    rate = serializers.IntegerField()
    comment = serializers.CharField()
    created_at = serializers.DateTimeField()
