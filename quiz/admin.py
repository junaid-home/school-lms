from quiz.models import Quizz, Question
from django.contrib import admin


class QuizListItemAdmin(admin.TabularInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuizListItemAdmin]

    class Meta:
        model = Quizz


admin.site.register(Quizz, QuizAdmin)
# admin.site.register(Question)
