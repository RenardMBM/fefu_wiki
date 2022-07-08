from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from comment.models import Comment
from comment.serializers import CommentSerializer

__all__ = ['CommentViewSet']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['head', 'get', 'post']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['teacher_article']
    ordering_fields = ['created_at']
    ordering = ['created_at']
