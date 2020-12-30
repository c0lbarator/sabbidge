from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article
from django.urls import reverse
def index(request):
    larlist = Article.objects.order_by('-date')
    return render(request, 'articles/list.html', {'larlist': larlist})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена!')

    lclist = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'lclist':lclist})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена!')

    a.comment_set.create(au_name = request.POST['name'], comment = request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))