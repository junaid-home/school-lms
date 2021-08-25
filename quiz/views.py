from json import loads
from results.models import Result
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Quizz, Question
from users.decorators import allowed_only


@allowed_only(roles=["Admin", 'Student'])
def quizz_view(request):
    quizz_list = Quizz.objects.filter(
        course__grade=request.user.grade).exclude(attempted_students__id=request.user.id)
    context = {'quizz_list': quizz_list}
    return render(request, 'quiz/quizz_list.html', context)


@allowed_only(roles=["Admin", 'Student'])
def single_quizz_view(request, Id):
    quizz = Question.objects.filter(
        quiz__course__grade=request.user.grade, quiz__id=Id).exclude(quiz__attempted_students__id=request.user.id)
    context = {'quizz_id': Id, 'bread_title': 'Quiz is Started!', 'bread_icon': 'command',
               'bread_subtitle': "Please check all of your answers before submitting once you submitted there is no way of going back"}

    if len(quizz) == 0:
        return redirect('404')

    return render(request, 'quiz/single_quizz.html', context)


@allowed_only(roles=["Admin", 'Student'])
def send_questions_as_json(request, Id):
    try:
        quizz = Quizz.objects.get(id=Id, course__grade=request.user.grade)
        quizz_questions = Question.objects.filter(
            quiz__course__grade=request.user.grade, quiz__id=Id).exclude(quiz__attempted_students__id=request.user.id)

        quizz_list = list(quizz_questions)
        filtered_quizz_list = []

        for question in quizz_list:
            object_dict = model_to_dict(question)
            del object_dict['answer']
            filtered_quizz_list.append(object_dict)

        quizz.attempted_students.add(request.user)
        quizz.save()

        return JsonResponse({'questions': filtered_quizz_list, 'time': quizz.time_in_minutes}, safe=False)
    except:
        return redirect('404')


@allowed_only(roles=["Admin", 'Student'])
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
        return JsonResponse({'status': 'Ok'})

    return JsonResponse({"message": 'Please make a POST request for saving data'})
