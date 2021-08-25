from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from lessons.models import Course
from .models import User
from .decorators import unauth_only, allowed_only


@unauth_only
def handle_login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        remember = None
        try:
            remember = request.POST['remember']
        except:
            remember = 'off'

        try:
            User.objects.get(user_name=user_name)
        except:
            messages.error(request, "No User exist with this \"Username\"")
            return render(request, 'users/login.html')

        user = authenticate(request, user_name=user_name, password=password)
        if user is not None:
            login(request, user)
            if remember == 'off':
                request.session.set_expiry(0)
            if request.user.role == 'Admin' or request.user.role == 'Student':
                return redirect('home')
            else:
                return redirect('parent')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')


@allowed_only(roles=["Admin", 'Student', 'Parent'])
def handle_logout(request):
    logout(request)
    return redirect('login')


@allowed_only(roles=["Admin", 'Student', 'Parent'])
def show_user_data(request):
    courses = Course.objects.filter(grade=request.user.grade)
    return render(request, 'users/profile.html', {"courses": courses})
