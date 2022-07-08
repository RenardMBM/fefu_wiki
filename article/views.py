from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from article.models import *
from article.serializers import *
from article.filters import *

__all__ = ['UniversityViewSet', 'TeacherViewSet']


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = UniversityArticle.objects.all()
    http_method_names = ['head', 'get', 'post']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title']
    ordering = ['title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortUniversitySerializer
        return UniversitySerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherArticle.objects.all()
    http_method_names = ['head', 'get', 'post']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, NearBirthdayFilter]
    filterset_fields = ['universities']
    ordering_fields = ['full_name', 'easy__rate']
    ordering = ['full_name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortTeacherSerializer
        return TeacherSerializer
