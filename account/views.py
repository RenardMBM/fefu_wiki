from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view

from account.models import User
from account.serializers import UserSerializer
from account.services import *


class UserViewSet(viewsets.ModelViewSet):  # TODO: только админ
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['head', 'get']


# TODO: Связь с vue
# def index(request, *args, **kwargs):
#     user = User.objects.prefetch_related('staff_for', 'student_for').get(pk=request.user.id)
#     user_data = json.dumps(UserSerializer(instance=user).data)
#     return render(request, 'index.html', context=dict(user_data=user_data))

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


@login_required
@api_view(['GET'])
def logout_view(request):
    logout(request)
    return redirect('/')
