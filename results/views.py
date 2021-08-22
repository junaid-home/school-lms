from django.shortcuts import render


def renderResults(request):
    return render(request, 'results/results.html')
