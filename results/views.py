from django.shortcuts import redirect, render
from lessons.models import Course
from .models import Result, SubjectResult
from users.decorators import allowed_only


@allowed_only(roles=["Admin", 'Student'])
def renderResults(request):
    courses = Course.objects.filter(grade=request.user.grade)
    results = Result.objects.filter(user=request.user)

    context = {'courses': courses, 'results': results, 'bread_title': 'Your Results',
               'bread_subtitle': "View your latest results and scores from below", 'bread_icon': 'award'}

    return render(request, 'results/results.html', context)


@allowed_only(roles=["Admin", 'Student'])
def renderSingleResult(request, Id):
    courses = Course.objects.filter(grade=request.user.grade)
    results = SubjectResult.objects.filter(
        result__id=Id, course__grade=request.user.grade)

    if len(results) == 0:
        return redirect('404')

    context = {'table_title': results[0].result.name, 'courses': courses, 'result': results, 'bread_title': 'Your Results',
               'bread_subtitle': 'View your latest results and scores from below', 'bread_icon': 'award'}

    return render(request, 'results/result_data.html', context)
