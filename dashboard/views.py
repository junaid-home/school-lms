from django.db import connections
from django.shortcuts import render
from lessons.models import Course


def dashboardView(request):
    courses = Course.objects.filter(grade=request.user.grade)
    return render(request, 'dashboard/home.html', {'courses': courses})


def notFoundView(request):
    return render(request, '404.html')
