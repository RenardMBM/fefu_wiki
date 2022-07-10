from django.shortcuts import get_object_or_404, HttpResponse, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import api_view, permission_classes

from article.filters import *
from article.models import *
from article.serializers import *

__all__ = ['UniversityViewSet', 'TeacherViewSet', 'change_teacher_rate']


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

    def get_permissions(self):
        if self.action == 'create':
            _permissions = [permissions.IsAdminUser]
        else:
            _permissions = [permissions.AllowAny]
        return [permission() for permission in _permissions]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherArticle.objects.all()
    http_method_names = ['head', 'get', 'post']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,
                       NearBirthdayFilter, filters.SearchFilter]
    filterset_fields = ['universities']
    ordering_fields = ['full_name', 'easy__rate']
    ordering = ['full_name']
    search_fields = ['full_name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortTeacherSerializer
        return TeacherSerializer

    def get_permissions(self):
        if self.action == 'create':
            _permissions = [permissions.IsAdminUser]
        else:
            _permissions = [permissions.AllowAny]
        return [permission() for permission in _permissions]


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # TODO: test this
def change_teacher_rate(request, aid):
    try:
        # rate_name: str = request.data['rate_name'] # For best times)
        value: int = int(request.data['value'])

        if not (0 < value < 11):
            raise ValueError
    except (ValueError, KeyError):
        return HttpResponse(status=400)

    article: TeacherArticle = get_object_or_404(TeacherArticle, pk=aid)
    story: StoryTeacher = StoryTeacher.objects.get_or_create(author=request.user,
                                                             comment=article.easy)
    count = article.easy.storyteacher_set.count()
    article.easy.rate = (article.easy.rate * count + value) / count
    story.value = value
    article.easy.save()
    story.save()
    return redirect('../../')
