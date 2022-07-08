from django.shortcuts import get_object_or_404

from article_request.models import TeacherRequest, UniversityRequest
from article.models import TeacherArticle, UniversityArticle
from article_request.serializers import TeacherEditSerializer, UniversityEditSerializer
from backend_queue.worker.services import send_email

__all__ = ['proc_request']


def proc_request(accept: bool, message: str, article_type: str, rid: int):
    article_classes = {'university': UniversityRequest,
                       'teacher': TeacherRequest}
    article = get_object_or_404(article_classes[article_type], pk=rid)
    email = article.author.email
    if accept:
        accept_request(article, article_type)
    else:
        reject_request(article)

    send_email(email, 'Ответ на ваше предложение', message)


def accept_request(article_obj, article_type: str) -> None:
    article_functions = {'university': _accept_university_request,
                         'teacher': _accept_teacher_request}

    article_functions[article_type](article_obj)


def _accept_teacher_request(teacher_request: TeacherRequest) -> None:
    teacher_article = TeacherArticle(pk=teacher_request.teacher_article.id,
                                     **TeacherEditSerializer(instance=teacher_request).data)
    teacher_article.save()
    teacher_request.delete()


def _accept_university_request(university_request: UniversityRequest) -> None:
    university_article = UniversityArticle(pk=university_request.university_article.id,
                                           **UniversityEditSerializer(
                                               instance=university_request).data)
    university_article.save()
    university_request.delete()


def reject_request(article_obj) -> None:
    article_obj.delete()
