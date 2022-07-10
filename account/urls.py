from django.conf import settings
from django.urls import path

from account.views import auth, ms_login_view, logout_view

urlpatterns = [
    path(settings.MS_AZURE['REDIRECT_PATH'], auth),
    path('login/microsoft/', ms_login_view),
    path('logout/', logout_view),
]
