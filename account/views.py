import json

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework import permissions
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, permission_classes

from account.models import User
from account.serializers import UserSerializer
from account.services import *

__all__ = ['UserViewSet', 'index', 'ms_login_view', 'auth', 'logout_view']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['head', 'get']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'email']
    ordering = ['id']

    permission_classes = permissions.IsAdminUser


def index(request, *args, **kwargs):
    user_data = json.dumps(UserSerializer(instance=request.user).data)
    return render(request, 'index.html', context=dict(user_data=user_data))


def ms_login_view(request):
    request.session['flow'] = build_auth_code_flow(scopes=settings.MS_AZURE['SCOPE'])
    return redirect(request.session["flow"]["auth_uri"])


def auth(request):
    cache = load_cache(request)
    result = build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
        request.session.get("flow", {}), request.GET)
    if "error" in result:
        return redirect('/')  # TODO: ms auth exception

    save_cache(request, cache)
    user = authenticate(email=result.get("id_token_claims")['email'])
    login(request, user)

    return redirect('/')


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    logout(request)
    return redirect('/')
