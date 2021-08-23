from django.shortcuts import redirect, render
from lessons.models import Course, Video, Note


def renderCourse(request, subject, id):
    try:
        course = Course.objects.get(
            grade=request.user.grade, name=subject, id=id)
        courses = Course.objects.filter(grade=request.user.grade)
    except:
        return redirect('404')
    context = {'course': course, 'courses': courses}

    return render(request, 'lessons/course.html', context)


def renderCourseLectures(request, subject):
    try:
        courses = Course.objects.filter(grade=request.user.grade)
        videos = Video.objects.filter(
            grade=request.user.grade, course__name=subject)

        context = {'videos': videos, 'courses': courses, 'coursename': subject}
    except:
        return redirect('404')

    return render(request, 'lessons/lectures.html', context)


def renderCourseNotes(request, subject):
    try:
        courses = Course.objects.filter(grade=request.user.grade)
        notes = Note.objects.filter(
            grade=request.user.grade, course__name=subject)

        context = {'notes': notes, 'courses': courses, 'coursename': subject}
    except:
        return redirect('404')

    return render(request, 'lessons/notes.html', context)


def renderCourseLectureVideo(request, subject, videoId):
    try:
        courses = Course.objects.filter(grade=request.user.grade)
        video = Video.objects.get(
            grade=request.user.grade, course__name=subject, id=videoId)

        context = {'video': video, 'courses': courses, 'bread_title': 'Video Lecture',
                   'bread_subtitle': "View leacture from below"}
    except:
        return redirect('404')

    return render(request, 'lessons/single_lecture.html', context)


def renderCourseSingleNote(request, subject, noteId):
    try:
        courses = Course.objects.filter(grade=request.user.grade)
        note = Note.objects.get(
            grade=request.user.grade, course__name=subject, id=noteId)

        context = {'note': note, 'courses': courses, 'coursename': subject, 'bread_title': 'Lecture Notes',
                   'bread_subtitle': "View notes from below"}
    except:
        return redirect('404')

    return render(request, 'lessons/single_note.html', context)
