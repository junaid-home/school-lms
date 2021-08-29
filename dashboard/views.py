from django.db.models import Q
from django.http.response import JsonResponse
from dashboard.models import Attendence, Event, Fee, Period, School_timing
from django.shortcuts import redirect, render
from lessons.models import Course
from quiz.models import Quizz
from results.models import Result, SubjectResult
from users.models import Child
from math import floor
from users.decorators import allowed_only


@allowed_only(roles=["Admin", 'Student'])
def dashboard_view(request):
    courses = Course.objects.filter(grade=request.user.grade).count()
    events = Event.objects.filter().count()
    results = Result.objects.filter(user=request.user).count()
    attendence_list = Attendence.objects.filter(user__id=request.user.id)[0:6]
    fee_list = Fee.objects.filter(user__id=request.user.id)[0:6]
    quizz = Quizz.objects.filter(
        course__grade=request.user.grade).exclude(attempted_students__id=request.user.id).count()
    context = {'courses': courses, 'fee_list': fee_list, 'attendence_list': attendence_list, 'results': results, 'events': events, 'quizz': quizz, 'bread_title': "Student Dashboard",
               'bread_subtitle': "Welcome to student dashboard!", 'bread_icon': 'home'}
    return render(request, 'dashboard/home.html', context)


def handler404(request, exception):
    return render(request, '404.html')


def not_found_view(request):
    return render(request, '404.html')


@allowed_only(roles=["Admin", 'Student'])
def attendence_view(request):
    attendence_list = Attendence.objects.filter(user__id=request.user.id)
    context = {'table_title': 'Attendence Details',
               'attendence_list': attendence_list, 'bread_title': "Your Attendence", 'bread_icon': 'user', 'bread_subtitle': "Watch your attendece from below."}
    return render(request, 'dashboard/attendence.html', context)


@allowed_only(roles=["Admin", 'Student'])
def timetable_view(request):
    timetable = Period.objects.filter(timetable__grade=request.user.grade)

    context = {'table_title': 'Timetable Details',
               'timetable': timetable, 'bread_title': "Your Timetable", 'bread_icon': 'clock', 'bread_subtitle': "Please follow your timetable."}
    return render(request, 'dashboard/time_table.html', context)


@allowed_only(roles=["Admin", 'Student'])
def school_timing_view(request):
    timing = School_timing.objects.get()
    context = {'table_title': 'School Timing',
               'timing': timing, 'bread_title': "Your School Timing", 'bread_icon': 'watch', 'bread_subtitle': "Please strictly follow your school timings."}

    return render(request, 'dashboard/timing.html', context)


@allowed_only(roles=["Admin", 'Student'])
def school_events_view(request):
    events = Event.objects.filter()
    context = {'table_title': 'School Events',
               'events': events, 'bread_title': "Your School Events", 'bread_icon': 'zap', 'bread_subtitle': "Please follow the events timings."}

    return render(request, 'dashboard/events.html', context)


@allowed_only(roles=["Admin", 'Student'])
def student_fee_view(request):
    fee_list = Fee.objects.filter(user__id=request.user.id)
    context = {'table_title': 'Your Fee Status',
               'fee_list': fee_list, 'bread_title': "Fee Status", 'bread_icon': 'box', 'bread_subtitle': "Please submit all your dues in time."}

    return render(request, 'dashboard/fees.html', context)


@allowed_only(roles=['Parent'])
def parent_dashboard(request):
    childs = Child.objects.filter(parent=request.user)
    context = {'childs': childs, 'bread_title': "Dashboard", 'bread_icon': 'home',
               'bread_subtitle': "Welcome to your dashboard!"}
    return render(request, 'dashboard/parent.html', context)


@allowed_only(roles=['Parent'])
def child_stats(request, childId):
    _child = Child.objects.filter(child=childId, parent=request.user)
    if len(_child) == 0:
        return redirect('404')
    child = _child.all()[0].child
    quizz_results = Result.objects.filter(user__id=child.id, type='quizz')[0:6]
    sessional_results = Result.objects.filter(
        user__id=child.id, type='sessional')[0:3]
    attendence_list = Attendence.objects.filter(
        user__id=child.id)[0:6]
    fee_list = Fee.objects.filter(user__id=child.id)[0:6]

    context = {'fee_list': fee_list, 'attendence_list': attendence_list, 'child_grade': child.grade.name, 'sessional_results': sessional_results, 'quizz_results': quizz_results, 'bread_title': "Dashboard", 'bread_icon': 'home',
               'bread_subtitle': "Welcome to your dashboard!"}
    return render(request, 'dashboard/child-stats.html', context)


@allowed_only(roles=['Parent'])
def child_result(request, resultId, childGrade):
    try:
        result = SubjectResult.objects.filter(
            result__id=resultId, course__grade__name=childGrade)
        context = {'table_title': "Child Progress", 'result': result, 'bread_title': "Child Result", 'bread_icon': 'award',
                   'bread_subtitle': "View Your Child Progress"}

        return render(request, 'dashboard/child-result.html', context)
    except:
        return redirect('404')


@allowed_only(roles=['Admin', 'Student'])
def get_attendence_data_as_json(request):
    presents = Attendence.objects.filter(
        user__id=request.user.id, status="present").count()
    absents = Attendence.objects.filter(
        user__id=request.user.id, status="absent").count()
    total = Attendence.objects.filter(user__id=request.user.id).count()

    presents_percentage = floor(presents * 100 / total)
    absents_percentage = floor(absents * 100 / total)

    return JsonResponse({'data': [presents_percentage, absents_percentage]})


@allowed_only(roles=['Admin', 'Student'])
def get_result_data_as_json(request):
    results = Result.objects.filter(user=request.user, type="sessional")
    id = results.all()[0].id

    results = SubjectResult.objects.filter(
        result__id=id, course__grade=request.user.grade)

    data = {'subjects': [], 'marks': []}

    if len(results):
        for result in results.all():
            data['subjects'].append(result.course.name)
            data['marks'].append(
                floor(result.obtained_marks * 100 / result.total_marks))
    else:
        data['subjects'] = ['English', 'Urdu', "Math"]
        data['marks'] = [100, 100, 100]

    return JsonResponse({'data': data})
