from django.shortcuts import HttpResponse
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import api_view, permission_classes

from article_request.models import *
from article_request.serializers import *
from article_request.services import proc_request


__all__ = ['UniversityRequestViewSet', 'TeacherRequestViewSet', 'answer_article_request']


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


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated, permissions.IsAdminUser))  # TODO: test this
def answer_article_request(request, article_type, rid):
    article_classes = ('university', 'teacher')
    try:
        assert article_type in article_classes
        message: str = request.data['message']
        accept: bool = bool(request.data['accept'])
    except (AssertionError, ValueError, KeyError):
        return HttpResponse(status=400)

    proc_request(accept, message, article_type, rid)
