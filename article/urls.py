from django.urls import path

from article.views import UniversityList, TeacherList

urlpatterns = [
    path('api/university/', UniversityList.as_view(), name='get-universities'),
    path('api/teacher/', TeacherList.as_view(), name='get-teachers-by-filter'),
]
