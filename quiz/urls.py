from django.urls import path
from .views import get_questions_as_json, quizzView, recieve_quizz_data_as_json, singleQuizzView

urlpatterns = [
    path('quizz/', quizzView, name='quizz'),
    path('quizz/<int:Id>', singleQuizzView, name='quizz'),
    path('quizz/<int:Id>/data/', get_questions_as_json, name='quizz-data'),
    path('quizz/<int:Id>/data/save/',
         recieve_quizz_data_as_json, name='quizz-data-save')
]
