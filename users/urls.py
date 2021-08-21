from django.urls import path
from .views import handleLogin, handleLogout

urlpatterns = [
    path('login/', handleLogin, name='login'),
    path('logout/', handleLogout, name='logout')
]
