from dashboard.models import Attendence, Event, Fee, Period, School_timing
from django.db import connections
from django.shortcuts import render
from lessons.models import Course


def dashboardView(request):
    courses = Course.objects.filter(grade=request.user.grade)
    return render(request, 'dashboard/home.html', {'courses': courses})


def notFoundView(request):
    return render(request, '404.html')


def attendenceView(request):
    courses = Course.objects.filter(grade=request.user.grade)
    attendence_list = Attendence.objects.filter(user__id=request.user.id)
    context = {'table_title': 'Attendence Details',
               'attendence_list': attendence_list, 'courses': courses, 'bread_title': "Your Attendence", 'bread_subtitle': "Watch your attendece from below."}
    return render(request, 'dashboard/attendence.html', context)


def timeTableView(request):
    courses = Course.objects.filter(grade=request.user.grade)
    timetable = Period.objects.filter(timetable__grade=request.user.grade)

    context = {'table_title': 'Timetable Details',
               'timetable': timetable, 'courses': courses, 'bread_title': "Your Timetable", 'bread_subtitle': "Please follow your timetable."}
    return render(request, 'dashboard/time_table.html', context)


def schoolTimingView(request):
    courses = Course.objects.filter(grade=request.user.grade)
    timing = School_timing.objects.get()
    context = {'table_title': 'School Timing',
               'timing': timing, 'courses': courses, 'bread_title': "Your School Timing", 'bread_subtitle': "Please strictly follow your school timings."}

    return render(request, 'dashboard/timing.html', context)


def schoolEventsView(request):
    courses = Course.objects.filter(grade=request.user.grade)
    events = Event.objects.filter()
    context = {'table_title': 'School Events',
               'events': events, 'courses': courses, 'bread_title': "Your School Events", 'bread_subtitle': "Please follow the events timings."}

    return render(request, 'dashboard/events.html', context)


def studentFeeView(request):
    courses = Course.objects.filter(grade=request.user.grade)
    fee_list = Fee.objects.filter(user__id=request.user.id)
    context = {'table_title': 'Your Fee Status',
               'fee_list': fee_list, 'courses': courses, 'bread_title': "Fee Status", 'bread_subtitle': "Please submit all your dues in time."}

    return render(request, 'dashboard/fees.html', context)
