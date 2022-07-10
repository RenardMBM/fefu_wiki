from django.db.models.signals import pre_save
from django.dispatch import receiver

from comment.models import Comment, CommentRating


@receiver(pre_save, sender=Comment)
def save_or_create_teacher(sender, instance: Comment, **kwargs):
    if instance.like:
        instance.like = CommentRating.objects.create()

    else:
        try:
            instance.like.save()

        except CommentRating.DoesNotExist:
            instance.like = CommentRating.objects.create()

    if instance.dislike:
        instance.dislike = CommentRating.objects.create()

    else:
        try:
            instance.dislike.save()

        except CommentRating.DoesNotExist:
            instance.dislike = CommentRating.objects.create()
