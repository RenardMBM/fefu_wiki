from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from article.models import UniversityArticle, TeacherArticle, TeacherRating
from account.models import User

__all__ = ['UniversityRequest', 'TeacherRequest']


class UniversityRequest(UniversityArticle):
    university_article = models.ForeignKey(UniversityArticle, on_delete=models.CASCADE,
                                           related_name="+")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = None


class TeacherRequest(TeacherArticle):
    teacher_article = models.ForeignKey(TeacherArticle, on_delete=models.CASCADE, related_name="+")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = None


@receiver(pre_save, sender=TeacherRequest)  # TODO: упростить, исправить
def save_or_create_teacher(sender: TeacherRequest, instance: TeacherRequest,  **kwargs):
    if sender.easy:
        instance.easy = TeacherRating.objects.create()
        instance.easy.save()

    else:
        try:
            instance.easy.save()

        except ObjectDoesNotExist:
            instance.easy = TeacherRating.objects.create()
            instance.easy.save()
