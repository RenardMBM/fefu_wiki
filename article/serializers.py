from rest_framework import serializers

from article.models import *

__all__ = ['ShortUniversitySerializer', 'UniversitySerializer',
           'ShortTeacherSerializer', 'TeacherSerializer']


class ShortUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityArticle
        fields = ['id', 'title']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityArticle
        fields = ['id', 'title', 'content']


# Teacher

class TeacherRaitingSerializer(serializers.ModelSerializer):
    last_rate = serializers.SerializerMethodField()

    def get_last_rate(self, obj):
        uid = self.context['request'].user.id
        if uid and obj.storyteacher_set.exists():
            try:
                last_story = obj.storyteacher_set.select_related('author').get(id=uid)

                if last_story:
                    return last_story.value
            except StoryTeacher.DoesNotExist:
                pass
        return 0

    class Meta:
        model = TeacherRating
        fields = ['rate', 'last_rate']


class ShortTeacherSerializer(serializers.ModelSerializer):
    easy = TeacherRaitingSerializer(read_only=True)
    full_birthday = serializers.SerializerMethodField()

    def get_full_birthday(self, obj):
        return obj.birthday.replace(year=obj.birth_year)

    class Meta:
        model = TeacherArticle
        fields = ['id', 'full_name', 'easy', 'full_birthday']


class TeacherSerializer(serializers.ModelSerializer):
    easy = TeacherRaitingSerializer(read_only=True)
    full_birthday = serializers.SerializerMethodField()
    teacher_birthday = serializers.DateField(write_only=True)
    universities = ShortUniversitySerializer(many=True)

    def get_full_birthday(self, obj):
        return obj.birthday.replace(year=obj.birth_year)

    def create(self, validated_data):
        birthday = validated_data['teacher_birthday']
        universities = validated_data['universities']
        del validated_data['teacher_birthday']
        del validated_data['universities']
        birth_year = birthday.year
        birthday = birthday.replace(year=2020)
        teacher_article = TeacherArticle.objects.create(birthday=birthday,
                                                        birth_year=birth_year,
                                                        **validated_data)
        for university in universities:
            teacher_article.universities.add(university)
        teacher_article.save()
        return teacher_article

    class Meta:
        model = TeacherArticle
        exclude = ['birthday', 'birth_year', 'created_at', 'updated_at']
