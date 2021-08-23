from django.contrib import admin
from dashboard.models import Attendence, Event, Fee, School_timing, Timetable, Period


class PeriodInlineAdminField(admin.TabularInline):
    model = Period


class TimetableAdmin(admin.ModelAdmin):
    inlines = [PeriodInlineAdminField]

    class Meta:
        model = Timetable


admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Attendence)
admin.site.register(School_timing)
admin.site.register(Event)
admin.site.register(Fee)
