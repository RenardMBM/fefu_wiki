from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from account.views import UserViewSet
from article.views import UniversityViewSet, TeacherViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'article/university', UniversityViewSet)
router.register(r'article/teacher', TeacherViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('comment.urls')),
    path('', include('account.urls')),
]
