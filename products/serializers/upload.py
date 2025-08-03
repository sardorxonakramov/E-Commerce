from rest_framework import serializers

from Common.choices.size import QualityChoice
from products.models import Upload


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ("id", "file", "quality")
        read_only_fields = ("id",)

    def validate_quality(self, value):
        if value not in [choice[0] for choice in QualityChoice.choices]:
            raise serializers.ValidationError("Invalid quality choice.")
        return value
