from django.urls import path

from comment.views import change_comment_rate

urlpatterns = [
    path('api/comment/<int:cid>/change_rate/', change_comment_rate),
]
