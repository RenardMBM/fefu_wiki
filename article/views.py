from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.generics import ListCreateAPIView

from article.models import *
from article.serializers import *
from article.filters import *

__all__ = ['UniversityList', 'TeacherList']


class UniversityList(ListCreateAPIView):
    queryset = UniversityArticle.objects.all()
    serializer_class = ShortUniversitySerializer

    page_size = 15
    page_size_query_param = 'count'
    max_page_size = 50

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title']
    ordering = ['title']


class TeacherList(ListCreateAPIView):
    queryset = TeacherArticle.objects.all()
    serializer_class = ShortTeacherSerializer

    page_size = 5
    page_size_query_param = 'count'
    max_page_size = 50

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, NearBirthdayFilter]
    filterset_fields = ['universities']
    ordering_fields = ['full_name', 'easy__rate']
    ordering = ['full_name']


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = TeacherArticle.objects.all()
