from rest_framework import serializers

from comment.models import *

__all__ = ['CommentSerializer']


class CommentRatingSerializer(serializers.ModelSerializer):
    last_rate = serializers.SerializerMethodField()

    def get_last_rate(self, obj):
        uid = self.context['request'].user.id
        if uid and obj.storycomment_set.exists():
            try:
                last_story = obj.storycomment_set.select_related('author').get(id=uid)

                if last_story:
                    return int(last_story.value)
            except StoryComment.DoesNotExist:
                pass
        return 0

    class Meta:
        model = CommentRating
        fields = ['rate', 'last_rate']


class CommentSerializer(serializers.ModelSerializer):
    like = CommentRatingSerializer(read_only=True)
    dislike = CommentRatingSerializer(read_only=True)

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        comment.author = self.context['request'].user
        comment.save()
        return comment

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']
        write_only_fields = ['teacher_article']
