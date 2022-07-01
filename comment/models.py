from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User
from article.models import TeacherArticle

__all__ = ['Comment']


class CommentRating(models.Model):
    rate = models.IntegerField(default=0)


class StoryComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BooleanField()
    comment = models.ForeignKey(CommentRating, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    teacher_article = models.ForeignKey(TeacherArticle, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(_('content'))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    like = models.OneToOneField(CommentRating, on_delete=models.CASCADE, related_name='+')
    dislike = models.OneToOneField(CommentRating, on_delete=models.CASCADE, related_name='+')
