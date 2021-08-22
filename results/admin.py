from django.contrib import admin
from .models import Result, SubjectResult


class SubjectResultAdmin(admin.TabularInline):
    model = SubjectResult


class ResultAdmin(admin.ModelAdmin):
    inlines = [SubjectResultAdmin]

    class Meta:
        model = Result


admin.site.register(Result, ResultAdmin)
admin.site.register(SubjectResult)
