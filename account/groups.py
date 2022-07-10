from dataclasses import dataclass

from django.contrib.auth.models import Group

__all__ = ['GROUPS', 'register_groups']


@dataclass
class Groups:
    moderator: str = 'moderator'
    client: str = 'client'

    def all(self) -> list:
        return [self.moderator, self.client]


GROUPS = Groups()


def register_groups():
    for group in GROUPS.all():
        Group.objects.get_or_create(name=group)
