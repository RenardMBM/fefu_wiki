from rest_framework import viewsets, filters

from article_request.models import *
from article_request.serializers import *

__all__ = ['UniversityRequestViewSet', 'TeacherRequestViewSet']


class UniversityRequestViewSet(viewsets.ModelViewSet):
    queryset = UniversityRequest.objects.all()
    http_method_names = ['head', 'get', 'post']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'created_at']
    ordering = ['title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortUniversityRequestSerializer
        return UniversityRequestSerializer


class TeacherRequestViewSet(viewsets.ModelViewSet):
    queryset = TeacherRequest.objects.all()
    http_method_names = ['head', 'get', 'post']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['full_name', 'created_at']
    ordering = ['full_name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortTeacherRequestSerializer
        return TeacherRequestSerializer
