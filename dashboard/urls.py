from django.urls import path
from .views import attendenceView, dashboardView, notFoundView, timeTableView

urlpatterns = [
    path('dashboard/', dashboardView, name='home'),
    path('attendence/', attendenceView, name='attendence'),
    path('timetable/', timeTableView, name='timetable'),
    path('404/', notFoundView, name="404")
]
