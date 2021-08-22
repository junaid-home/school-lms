from django.urls import path
from .views import dashboardView, notFoundView

urlpatterns = [
    path('dashboard/', dashboardView, name='home'),
    path('404/', notFoundView, name="404")
]
