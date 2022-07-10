from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from account.models import User
from article.models import UniversityArticle, TeacherArticle, TeacherRating

__all__ = ['UniversityRequest', 'TeacherRequest']


class UniversityRequest(UniversityArticle):
    university_article = models.ForeignKey(UniversityArticle, on_delete=models.CASCADE,
                                           related_name="+")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        try:
            result = f' | {str(self.university_article)}'
        except ObjectDoesNotExist:
            result = ''
        return f"Change university ({self.id})" + result

    class Meta:
        verbose_name = "Request to change the university"
        verbose_name_plural = "Requests to change the university"


class TeacherRequest(TeacherArticle):
    teacher_article = models.ForeignKey(TeacherArticle, on_delete=models.CASCADE, related_name="+")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        try:
            result = f' | {str(self.teacher_article)}'
        except ObjectDoesNotExist:
            result = ''
        return f"Change teacher ({self.id})" + result

    class Meta:
        verbose_name = "Request to change the teacher"
        verbose_name_plural = "Requests to change the teacher"
