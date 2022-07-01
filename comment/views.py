from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.generics import ListCreateAPIView

from comment.models import *
from comment.serializers import CommentSerializer

__all__ = ['CommentList']


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    page_size = 10
    page_size_query_param = 'count'
    max_page_size = 50

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['teacher_article']
    ordering_fields = ['created_at']
    ordering = ['created_at']
