from django.urls import path
from .views import handle_login, handle_logout, show_user_data
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', handle_login, name='login'),
    path('logout/', handle_logout, name='logout'),
    path('profile/', show_user_data, name='profile'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"),
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/reset.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"),
         name="password_reset_complete"),
]
