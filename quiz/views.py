from json import loads
from results.models import Result
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Quizz, Question
from lessons.models import Course


def quizzView(request):
    courses = Course.objects.filter(grade=request.user.grade)
    quizz_list = Quizz.objects.filter(
        course__grade=request.user.grade).exclude(attempted_students__id=request.user.id)
    context = {'quizz_list': quizz_list, 'courses': courses}
    return render(request, 'quiz/quizz_list.html', context)


def singleQuizzView(request, Id):
    courses = Course.objects.filter(grade=request.user.grade)
    quizz = Question.objects.filter(
        quiz__course__grade=request.user.grade, quiz__id=Id).exclude(quiz__attempted_students__id=request.user.id)
    context = {'courses': courses, 'quizz_id': Id, 'bread_title': 'Quiz is Started!',
               'bread_subtitle': "Please check all of your answers before submitting once you submitted there is no way of going back"}

    if len(quizz) == 0:
        return redirect('404')

    return render(request, 'quiz/single_quizz.html', context)


def get_questions_as_json(request, Id):
    quizz = Question.objects.filter(
        quiz__course__grade=request.user.grade, quiz__id=Id).exclude(quiz__attempted_students__id=request.user.id)

    quizz_list = list(quizz)
    filtered_quizz_list = []

    for question in quizz_list:
        object_dict = model_to_dict(question)
        del object_dict['answer']
        filtered_quizz_list.append(object_dict)

    return JsonResponse(filtered_quizz_list, safe=False)


def recieve_quizz_data_as_json(request, Id):
    if request.method == 'POST':
        quizz = Quizz.objects.get(id=Id, course__grade=request.user.grade)
        total_questions = quizz.total_questions
        _score = 0
        status = 'failed'
        mutiplier = 100 / total_questions
        quizz_data = loads(request.body)

        for q in quizz_data:
            for k in q.keys():
                try:
                    Question.objects.get(question=k, answer=q[k])
                    _score += 1
                except:
                    pass

        score = round(_score * mutiplier)
        if score > quizz.passing_percentage:
            status = 'passed'

        color = 'green' if status == 'passed' else 'red'
        result = Result(name=quizz.title, type="quizz",
                        total_marks=100, obtained_marks=score, status=status, user=request.user, color=color)

        result.save()
        quizz.attempted_students.add(request.user)
        quizz.save()
        return JsonResponse({'status': 'Ok'})

    return JsonResponse({"message": 'Please make a POST request for saving data'})