from django.shortcuts import get_object_or_404, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import api_view, permission_classes

from comment.models import Comment, StoryComment
from comment.serializers import CommentSerializer

__all__ = ['CommentViewSet', 'change_comment_rate']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['head', 'get', 'post']

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['teacher_article']
    ordering_fields = ['created_at']
    ordering = ['created_at']


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # TODO: test this
def change_comment_rate(request, cid):
    try:
        value: int = int(request.data['value'])

        if not (-2 < value < 2):
            raise ValueError
    except (ValueError, KeyError):
        return HttpResponse(status=400)

    article: Comment = get_object_or_404(Comment, pk=cid)
    like_story: StoryComment = StoryComment.objects.get_or_create(author=request.user,
                                                                  comment=article.like)
    dislike_story: StoryComment = StoryComment.objects.get_or_create(author=request.user,
                                                                     comment=article.dislike)
    if value == 1:
        if not like_story.value:
            article.like.rate += 1
            like_story.value = True
        if dislike_story.value:
            article.dislike.rate -= 1
            dislike_story.value = False

    elif value == -1:
        if not dislike_story.value:
            article.dislike.rate += 1
            dislike_story.value = True
        if like_story.value:
            article.like.rate -= 1
            like_story.value = False

    article.like.save()
    article.dislike.save()
    like_story.save()
    dislike_story.save()
