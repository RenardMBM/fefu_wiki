from rest_framework import serializers

from account.models import User

__all__ = ['UserSerializer']


class UserSerializer(serializers.ModelSerializer):
    access_level = serializers.SerializerMethodField()

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
