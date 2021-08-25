from django.urls import path
from .views import course_lecture_video_view, course_lectures_view, course_notes_article_view, course_notes_view, courses_view

urlpatterns = [
    path('courses/', courses_view, name='courses'),
    path('<str:subject>/lectures/', course_lectures_view, name='lectures'),
    path('<str:subject>/lectures/<int:videoId>/',
         course_lecture_video_view, name='lecture'),
    path('<str:subject>/notes/', course_notes_view, name='notes'),
    path('<str:subject>/notes/<int:noteId>/',
         course_notes_article_view, name='note'),
]
