from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        from account.signals import create_groups
        post_migrate.connect(create_groups, sender=self)
