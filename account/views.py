from rest_framework import viewsets

from account.models import User
from account.serializers import UserSerializer

__all__ = ['UserViewSet']


class UserViewSet(viewsets):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# TODO: Связь с vue
# def index(request, *args, **kwargs):
#     user = User.objects.prefetch_related('staff_for', 'student_for').get(pk=request.user.id)
#     user_data = json.dumps(UserSerializer(instance=user).data)
#     return render(request, 'index.html', context=dict(user_data=user_data))