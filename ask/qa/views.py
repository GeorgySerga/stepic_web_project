from django.http import HttpResponse
from qa.models import Question
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_list(request):
  page = request.GET.get('page', 1)
  if request.path == '/popular/':
    questions = Question.objects.popular()
  else:
    questions = Question.objects.new()

  paginatior = Paginator(questions, 10)
  page = paginator.page(page)

  return render(request, 'qa/templates/question_list.html', {
    'questions': page.object_list,
    'page': page
  })


def question_details(request, id):
  question = get_object_or_404(Question, id=id)
  return render(request, 'qa/templates/question_details.html', {
    'question': question
  })
