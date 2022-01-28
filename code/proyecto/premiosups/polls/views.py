from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', { 'latest_question_list': questions })

def detail(request, question_id):
    return HttpResponse(f'Estas viendo la pregunta numero {question_id}')

def results(request, question_id):
    return HttpResponse(f'Estas viendo los resultados de la pregunta numero {question_id}')

def vote(request, question_id):
    return HttpResponse(f'Estas votando a la pregunta numero {question_id}')