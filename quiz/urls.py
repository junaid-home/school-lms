from django.urls import path
from .views import send_questions_as_json, quizz_view, recieve_quizz_data_as_json, single_quizz_view

urlpatterns = [
    path('quizz/', quizz_view, name='quizz'),
    path('quizz/<int:Id>', single_quizz_view, name='quizz'),
    path('quizz/<int:Id>/data/', send_questions_as_json, name='quizz-data'),
    path('quizz/<int:Id>/data/save/',
         recieve_quizz_data_as_json, name='quizz-data-save')
]
