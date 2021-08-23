from django.urls import path
from .views import attendenceView, dashboardView, notFoundView, schoolEventsView, studentFeeView, timeTableView, schoolTimingView

urlpatterns = [
    path('dashboard/', dashboardView, name='home'),
    path('attendence/', attendenceView, name='attendence'),
    path('timetable/', timeTableView, name='timetable'),
    path('school-timing/', schoolTimingView, name='timing'),
    path('school-events/', schoolEventsView, name='events'),
    path('fee/', studentFeeView, name='fee'),
    path('404/', notFoundView, name="404")
]
