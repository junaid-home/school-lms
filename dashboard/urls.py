from django.urls import path
from .views import attendence_view, dashboard_view, not_found_view, school_events_view, student_fee_view, timetable_view, school_timing_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='home'),
    path('attendence/', attendence_view, name='attendence'),
    path('timetable/', timetable_view, name='timetable'),
    path('school-timing/', school_timing_view, name='timing'),
    path('school-events/', school_events_view, name='events'),
    path('fee/', student_fee_view, name='fee'),
    path('404/', not_found_view, name="404")
]
