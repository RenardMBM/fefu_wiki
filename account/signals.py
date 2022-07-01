from account.groups import register_groups

__all__ = ['create_groups']


def create_groups(sender, **kwargs):
    register_groups()
