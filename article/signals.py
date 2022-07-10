from django.db.models.signals import pre_save
from django.dispatch import receiver

from article.models import TeacherArticle, TeacherRating


@receiver(pre_save, sender=TeacherArticle)
def save_or_create_teacher(sender, instance: TeacherArticle, **kwargs):
    if instance.easy:
        instance.easy = TeacherRating.objects.create(teacherarticle=instance)

    else:
        try:
            instance.easy.save()

        except TeacherRating.DoesNotExist:
            instance.easy = TeacherRating.objects.create(teacherarticle=instance)
