from rest_framework import serializers

from comment.models import *

__all__ = ['CommentSerializer']


class CommentSerializer(serializers.ModelSerializer):
    voted = serializers.SerializerMethodField()
    # TODO: Дописать -1 отриц. 0 - не голос, 1 - голос

    class Meta:
        model = Comment
        exclude = ['teacher_article']


