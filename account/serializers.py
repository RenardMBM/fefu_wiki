from rest_framework import serializers

from account.models import User
from django.contrib.auth.models import AnonymousUser

__all__ = ['UserSerializer']


class UserSerializer(serializers.ModelSerializer):
    access_level = serializers.SerializerMethodField()

    def create(self, validated_data: dict):
        password = validated_data['password']
        validated_data['password'].pop()
        user = User.objects.create(**validated_data)
        user.set_password(password)

        return user.save()

    def get_access_level(self, obj):
        if obj.is_superuser:
            return 3
        if obj.is_staff:
            return 2
        if obj.is_authenticated():
            return 1
        return 0

    class Meta:
        model = User
        fields = ('email', 'access_level')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['access_level']
