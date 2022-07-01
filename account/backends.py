from django.contrib.auth.backends import ModelBackend

from account.models import User


class MyLoginBackend(ModelBackend):
    def authenticate(self, email=None, *args, **kwargs):
        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            return None

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)

        except User.DoesNotExist:
            return None
