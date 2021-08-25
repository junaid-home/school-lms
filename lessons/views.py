from django.shortcuts import redirect, render
from lessons.models import Course, Video, Note
from users.decorators import allowed_only


@allowed_only(roles=['Admin', 'Student'])
def courses_view(request):
    courses = Course.objects.filter(grade=request.user.grade)

    context = {'courses': courses, 'bread_title': 'My Courses',
               'bread_subtitle': "Here are all of your courses", 'bread_icon': 'book'}
    return render(request, 'lessons/courses.html', context)


@allowed_only(roles=["Admin", 'Student'])
def course_lectures_view(request, subject):
    try:

        videos = Video.objects.filter(
            grade=request.user.grade, course__name=subject)

        context = {'videos': videos, 'coursename': subject}
    except:
        return redirect('404')

    return render(request, 'lessons/lectures.html', context)


@allowed_only(roles=["Admin", 'Student'])
def course_notes_view(request, subject):
    try:

        notes = Note.objects.filter(
            grade=request.user.grade, course__name=subject)

        context = {'notes': notes, 'coursename': subject}
    except:
        return redirect('404')

    return render(request, 'lessons/notes.html', context)


@allowed_only(roles=["Admin", 'Student'])
def course_lecture_video_view(request, subject, videoId):
    try:

        video = Video.objects.get(
            grade=request.user.grade, course__name=subject, id=videoId)

        context = {'video': video, 'bread_title': 'Video Lecture',
                   'bread_subtitle': "View leacture from below", 'bread_icon': 'book'}
    except:
        return redirect('404')

    return render(request, 'lessons/single_lecture.html', context)


@allowed_only(roles=["Admin", 'Student'])
def course_notes_article_view(request, subject, noteId):
    try:

        note = Note.objects.get(
            grade=request.user.grade, course__name=subject, id=noteId)

        context = {'note': note, 'coursename': subject, 'bread_title': 'Lecture Notes',
                   'bread_subtitle': "View notes from below", 'bread_icon': 'book'}
    except:
        return redirect('404')

    return render(request, 'lessons/single_note.html', context)
