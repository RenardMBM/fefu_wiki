from django.urls import path

from comment.views import CommentList

urlpatterns = [
    path('api/comment/', CommentList.as_view()),
]
