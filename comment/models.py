from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from account.models import User
from article.models import TeacherArticle

__all__ = ['Comment', 'CommentRating', 'StoryComment']


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
    like = models.OneToOneField(CommentRating, on_delete=models.CASCADE, related_name='+', blank=True)
    dislike = models.OneToOneField(CommentRating, on_delete=models.CASCADE, related_name='+', blank=True)


@receiver(pre_save, sender=Comment)  # TODO: упростить, исправить
def save_or_create_teacher(sender: Comment, instance: Comment,  **kwargs):
    if sender.like:
        instance.like = CommentRating.objects.create()
        instance.like.save()

    else:
        try:
            instance.like.save()

        except ObjectDoesNotExist:
            instance.like = CommentRating.objects.create()
            instance.like.save()

    if sender.dislike:
        instance.dislike = CommentRating.objects.create()
        instance.dislike.save()

    else:
        try:
            instance.dislike.save()

        except ObjectDoesNotExist:
            instance.dislike = CommentRating.objects.create()
            instance.dislike.save()
