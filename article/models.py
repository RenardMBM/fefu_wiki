from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from account.models import User


__all__ = ['UniversityArticle', 'TeacherArticle', 'TeacherRating', 'StoryTeacher']


class UniversityArticle(models.Model):
    title = models.CharField(_('university title'), max_length=128)
    content = models.TextField()

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)


class TeacherRating(models.Model):
    rate = models.FloatField(default=0)


class StoryTeacher(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                         MaxValueValidator(10)])
    comment = models.ForeignKey(TeacherRating, on_delete=models.CASCADE)


class TeacherArticle(models.Model):
    universities = models.ManyToManyField(UniversityArticle)

    full_name = models.CharField(_('full name'), max_length=128)
    image = models.ImageField(_('profile img'))
    academic_degree = models.CharField(_('academic degree'), max_length=256)
    content = models.TextField()
    birthday = models.DateField(_("day and month of birth"))
    birth_year = models.IntegerField(_("year of birth"))
    easy = models.OneToOneField(TeacherRating, on_delete=models.CASCADE, blank=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)


@receiver(post_save, sender=TeacherArticle)
def save_or_create_teacher(sender, instance: TeacherArticle, created, **kwargs):
    if created and not instance.easy:
        TeacherRating.objects.create(teacherarticle=instance)

    else:
        try:
            instance.easy.save()

        except ObjectDoesNotExist:
            TeacherRating.objects.create(teacherarticle=instance)
