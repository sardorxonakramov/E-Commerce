from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "passport_series",
            "phone",
            "role",
            "date_joined",
        )
        read_only_fields = ("role", "date_joined")  # boshlang‘ich read-only maydonlar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Foydalanuvchi passport_series ni kiritgan bo‘lsa — read_only qilib qo‘yiladi
        instance = kwargs.get("instance", None)
        if instance and instance.passport_series:
            self.fields["passport_series"].read_only = True


from rest_framework import serializers
from django.contrib.auth import authenticate

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        user = self.context['request'].user
        old_password = attrs.get('old_password')

        if not user.check_password(old_password):
            raise serializers.ValidationError({"old_password": "Eski parol noto‘g‘ri"})

        new_password = attrs.get('new_password')
        new_password2 = attrs.get('new_password2')

        if new_password != new_password2:
            raise serializers.ValidationError({"new_password2": "Parollar mos emas"})

        if old_password == new_password:
            raise serializers.ValidationError({"new_password": "Yangi parol eski paroldan farqli bo‘lishi kerak"})

        return attrs
