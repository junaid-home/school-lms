from django.urls import path
from django.conf.urls import handler404
from .views import attendence_view, child_result, child_stats, dashboard_view, not_found_view, parent_dashboard, school_events_view, student_fee_view, timetable_view, school_timing_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='home'),
    path('attendence/', attendence_view, name='attendence'),
    path('timetable/', timetable_view, name='timetable'),
    path('school-timing/', school_timing_view, name='timing'),
    path('school-events/', school_events_view, name='events'),
    path('fee/', student_fee_view, name='fee'),
    path('404/', not_found_view, name="404"),
    path('parent/', parent_dashboard, name='parent'),
    path('child/result/<int:resultId>/<str:childGrade>/',
         child_result, name='child-result'),
    path('parent/child/<int:childId>/', child_stats, name='child'),
]

handler404 = 'dashboard.views.handler404'
