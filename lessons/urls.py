from django.urls import path
from .views import renderCourseLectures, renderCourseNotes, renderCourseLectureVideo, renderCourseSingleNote

urlpatterns = [
    path('<str:subject>/lectures/', renderCourseLectures, name='lectures'),
    path('<str:subject>/lectures/<int:videoId>/',
         renderCourseLectureVideo, name='lecture'),
    path('<str:subject>/notes/', renderCourseNotes, name='notes'),
    path('<str:subject>/notes/<int:noteId>/',
         renderCourseSingleNote, name='note'),
]
