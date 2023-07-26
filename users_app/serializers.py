from rest_framework import serializers

from .models import AvatarUser, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "fullName", "email", "phone", "balance", "avatar"]

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.fullName = validated_data.get('fullName', instance.fullName)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance


class AvatarSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = AvatarUser
        fields = ["src", "alt"]

    def get_src(self, obj):
        return obj.src.url


class ProfileSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer()

    class Meta:
        model = Profile
        fields = [
            "fullName",
            "email",
            "phone",
            "avatar",
        ]

    def update(self, instance, validated_data):
        instance.fullName = validated_data.get('fullName', instance.fullName)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


