from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import User


def handleLogin(request):
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
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')


def handleLogout(request):
    logout(request)
    return redirect('login')
