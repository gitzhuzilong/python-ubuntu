from django.contrib.auth import authenticate

from Api.utils import *

def admin_require(func):
    def _wrapper(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return not_authenticated()
        if not request.user.is_superuser:
            return permission_denied()
        return func(self, request, *args, **kwargs)
    return _wrapper
def customer_require(func):
    def _wrapper(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return not_authenticated()
        if not hasattr(user, 'customer'):
            return permission_denied()
        return func(self, request, *args, **kwargs)
    return _wrapper
            
def userinfo_require(func):
    def _wrapper(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return not_authenticated()
        if not hasattr(user, 'userinfo'):
            return permission_denied()
        return func(self, request, *args, **kwargs)
    return _wrapper
