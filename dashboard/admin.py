from django.contrib import admin
from dashboard.models import Attendence, Timetable, Period


class PeriodInlineAdminField(admin.TabularInline):
    model = Period


class TimetableAdmin(admin.ModelAdmin):
    inlines = [PeriodInlineAdminField]

    class Meta:
        model = Timetable


admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Attendence)
