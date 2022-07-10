from django.db.models.signals import pre_save
from django.dispatch import receiver

from article.models import TeacherRating
from article_request.models import TeacherRequest


@receiver(pre_save, sender=TeacherRequest)
def save_or_create_teacher(sender, instance: TeacherRequest, **kwargs):
    if instance.easy:
        instance.easy = TeacherRating.objects.create()

    else:
        try:
            instance.easy.save()

        except TeacherRating.DoesNotExist:
            instance.easy = TeacherRating.objects.create()
