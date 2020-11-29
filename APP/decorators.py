from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exist():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_fun(request, *args, **kwargs)
        return wrapper_func
    return decorator