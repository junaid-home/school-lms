from leave.views import add_new_leave_application, my_leave_applications
from django.urls import path

urlpatterns = [
    path('leaves/', my_leave_applications, name='leaves'),
    path('leave/new/', add_new_leave_application, name="new_leave")
]
