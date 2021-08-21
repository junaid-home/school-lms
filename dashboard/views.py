from django.shortcuts import render


def dashboardView(request):
    return render(request, 'dashboard/home.html')
