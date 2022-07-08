from django.contrib.auth.backends import ModelBackend

from account.models import User


class MSBackend(ModelBackend):
    def authenticate(self, request, email=None, *args, **kwargs):
        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            user = User(email=email)
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)

        except User.DoesNotExist:
            return None
