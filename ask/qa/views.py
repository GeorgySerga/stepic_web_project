from django.http import HttpResponse
from qa.models import Question
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def new(request):
    qs = Question.objects.all()
    qs = qs.order_by('-added_at')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('question_list') + '?page='

    return render(request, 'list.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def popular(request):
    qs = Question.objects.all()
    qs = qs.order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'list_rating.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })
