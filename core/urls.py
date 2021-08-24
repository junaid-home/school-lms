from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('dashboard.urls')),
    path('', include('results.urls')),
    path('', include('lessons.urls')),
    path('', include('quiz.urls')),
    path('', include('leave.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin Dashboard Portal"
