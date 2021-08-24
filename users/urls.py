from django.urls import path
from .views import handle_login, handle_logout, show_user_data

urlpatterns = [
    path('login/', handle_login, name='login'),
    path('logout/', handle_logout, name='logout'),
    path('profile/', show_user_data, name='profile')
]
