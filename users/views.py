from django.shortcuts import render


def handleLogin(request):
    return render(request, 'users/login.html')
