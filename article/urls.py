from django.urls import path

from article.views import change_teacher_rate

urlpatterns = [
    path('api/article/teacher/<int:aid>/change_rate/', change_teacher_rate,),
]
