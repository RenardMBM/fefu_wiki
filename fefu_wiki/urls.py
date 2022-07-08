from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from account.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('article.urls')),
    path('', include('comment.urls')),
    path('', include('account.urls')),
]
