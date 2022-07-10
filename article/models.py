from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User

__all__ = ['UniversityArticle', 'TeacherArticle', 'TeacherRating', 'StoryTeacher']


class UniversityArticle(models.Model):
    title = models.CharField(_('university title'), max_length=128)
    content = models.TextField()

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return f'University ({self.id}) | {self.title}'

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class TeacherRating(models.Model):
    rate = models.FloatField(default=0)

    def short_name(self):
        return f"Teacher's rating ({self.id})"

    def get_teacher_name(self):
        try:
            return self.teacherarticle.full_name

        except ObjectDoesNotExist:
            return 'None'

    def get_teacher_name_or_short(self):
        result = self.get_teacher_name()

        if result == 'None':
            return self.short_name()
        return result

    def __str__(self):
        result = self.get_teacher_name()
        if result == 'None':
            result = ''
        else:
            result = ' | ' + result

        return self.short_name() + result

    class Meta:
        verbose_name = "Teacher's rating"
        verbose_name_plural = "Teacher's ratings"


class StoryTeacher(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                         MaxValueValidator(10)])
    comment = models.ForeignKey(TeacherRating, on_delete=models.CASCADE)

    def __str__(self):
        try:
            by = self.author.email
        except ObjectDoesNotExist:
            by = "None"

        try:
            to = self.comment.get_teacher_name_or_short()
        except ObjectDoesNotExist:
            to = 'None'

        return f"Teacher rate ({self.id}) | {by} -> {to}"

    class Meta:
        verbose_name = "Rate by user"
        verbose_name_plural = "Rates by user"


class TeacherArticle(models.Model):
    universities = models.ManyToManyField(UniversityArticle)

    full_name = models.CharField(_('full name'), max_length=128)
    image = models.ImageField(_('profile img'), upload_to='teacher/', default='default.png')
    academic_degree = models.CharField(_('academic degree'), max_length=256)
    content = models.TextField()
    birthday = models.DateField(_("day and month of birth"))
    birth_year = models.IntegerField(_("year of birth"))
    easy = models.OneToOneField(TeacherRating, on_delete=models.CASCADE, blank=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f'Teacher ({self.id}) | {self.full_name}'

    class Meta:
        verbose_name = 'Teacher'
