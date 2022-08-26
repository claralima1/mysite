from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("Você está olhando para a pergunta %s." % question_id)

def results(request, question_id):
    response = "Você está vendo os resultados da pergunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na pergunta %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Deixa o resto das visualizações (detalhe, resultados, votação) inalteradas.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})