from rest_framework import serializers

from article_request.models import *
from article.serializers import TeacherSerializer

__all__ = ['ShortUniversityRequestSerializer', 'UniversityRequestSerializer',
           'TeacherRequestSerializer', 'ShortTeacherRequestSerializer']


class ShortUniversityRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityRequest
        fields = ['title', 'created_at']


class UniversityRequestSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        university_request = UniversityRequest.objects.create(author=self.context['request'].user,
                                                              **validated_data)
        university_request.save()
        return university_request

    class Meta:
        model = UniversityRequest
        exclude = ['author']


# Teacher
class TeacherRequestSerializer(TeacherSerializer):
    def create(self, validated_data):
        birthday = validated_data['teacher_birthday']
        universities = validated_data['universities']
        del validated_data['teacher_birthday']
        del validated_data['universities']
        birth_year = birthday.year
        birthday = birthday.replace(year=2020)
        teacher_request = TeacherRequest.objects.create(birthday=birthday,
                                                        birth_year=birth_year,
                                                        author=self.context['request'].user,
                                                        **validated_data)
        for university in universities:
            teacher_request.universities.add(university)
        teacher_request.save()
        return teacher_request

    class Meta:
        model = TeacherRequest
        exclude = ['author', 'birthday', 'birth_year', 'created_at', 'updated_at']


class ShortTeacherRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherRequest
        fields = ['full_name', 'created_at']
