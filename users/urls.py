from django.urls import path
from .views import handleLogin

urlpatterns = [
    path('login/', handleLogin, name='login')
]
