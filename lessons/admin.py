from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Video, Course, Note, Grade


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, MyModelAdmin)
admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(Note)
