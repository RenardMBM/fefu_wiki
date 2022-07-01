from rest_framework import serializers

from article.models import *

__all__ = ['ShortUniversitySerializer', 'ShortTeacherSerializer', 'TeacherSerializer']


class ShortUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityArticle
        fields = ['id', 'title']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityArticle
        fields = ['title', 'content']


# Teacher
class ShortTeacherSerializer(serializers.ModelSerializer):
    full_birthday = serializers.SerializerMethodField()

    def get_full_birthday(self, obj):
        return obj.birthday.replace(year=obj.birth_year)

    class Meta:
        model = TeacherArticle
        fields = ['id', 'full_name', 'easy', 'full_birthday']  # TODO: Серелизатор для Rating(easy)


class TeacherSerializer(serializers.ModelSerializer):
    rating_free = serializers.IntegerField(default=5)
    full_birthday = serializers.SerializerMethodField()

    def get_full_birthday(self, obj):
        return obj.birthday.replace(year=obj.birth_year)

    class Meta:
        model = TeacherArticle
        exclude = ['created_at', 'updated_at']
