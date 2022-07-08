from django.conf import settings
import msal

__all__ = ['load_cache', 'save_cache', 'build_msal_app', 'build_auth_code_flow']
_TOKEN_CACHE = 'token_cache'


def load_cache(request):
    cache = msal.SerializableTokenCache()
    if request.session.get(_TOKEN_CACHE):
        cache.deserialize(request.session[_TOKEN_CACHE])
    return cache


def save_cache(request, cache):
    if cache.has_state_changed:
        request.session[_TOKEN_CACHE] = cache.serialize()


def build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        settings.MS_AZURE['CLIENT_ID'],
        authority=authority or settings.MS_AZURE['AUTHORITY'],
        client_credential=settings.MS_AZURE['CLIENT_SECRET'], token_cache=cache)


def build_auth_code_flow(authority=None, scopes=None):
    return build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [],
        redirect_uri=settings.MS_AZURE['FULL_REDIRECT_PATH'])
