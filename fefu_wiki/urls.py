from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from account.views import UserViewSet, index
from article.views import UniversityViewSet, TeacherViewSet
from article_request.views import UniversityRequestViewSet, TeacherRequestViewSet
from comment.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'article/university', UniversityViewSet)
router.register(r'article/teacher', TeacherViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'article_request/university', UniversityRequestViewSet)
router.register(r'article_request/teacher', TeacherRequestViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('article.urls')),
    path('', include('article_request.urls')),
    path('', include('comment.urls')),
    re_path(r"^.*$", index, name='index'),
]
