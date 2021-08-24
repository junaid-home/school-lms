from django.shortcuts import redirect, render
from django.contrib import messages
from .models import LeaveApplication
from .forms import LeaveApplicationForm


def my_leave_applications(request):
    applications = LeaveApplication.objects.filter(user=request.user)

    context = {'applications': applications, 'bread_title': "My Applications",
               "bread_subtitle": "View Complete List of your Applications History", "table_title": "Leave Applications"}

    return render(request, 'leave/applications_list.html', context)


def add_new_leave_application(request):
    if request.method == 'POST':
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        description = request.POST['description']
        type = request.POST['type']
        try:
            application = LeaveApplication(type=type, date_to=date_to, date_from=date_from,
                                           description=description, user=request.user, status='pending')
            application.save()
            return redirect('leaves')
        except:
            messages.error(
                request, "Failed to send leave Application request, are you sure you are connected to the internet!")

    form = LeaveApplicationForm()
    context = {'form': form, 'bread_title': "Send Leave Application",
               'bread_subtitle': "Please fill out the form correctly before sending leave request!"}

    return render(request, 'leave/new_application.html', context)
