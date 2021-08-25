from dashboard.models import Attendence, Event, Fee, Period, School_timing
from django.shortcuts import render
from lessons.models import Course
from quiz.models import Quizz
from results.models import Result
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
