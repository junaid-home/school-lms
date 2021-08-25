from django.shortcuts import redirect
from django.contrib.auth import logout


def unauth_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'student' or request.user.role == 'admin':
                return redirect('home')
            else:
                return redirect('home')

        return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_only(roles=[]):
    """
        Function which takes roles as list and only allowed that roles to access the current route
        @param roles
             @allowed roles ['Admin', 'Parent', 'Student']
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')

            if request.user.role in roles:
                return view_func(request, *args, **kwargs)
            else:
                logout(request)
                return redirect('login')

        return wrapper_func
    return decorator
