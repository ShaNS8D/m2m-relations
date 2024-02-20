from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles_list = Article.objects.all()
    # .order_by('scopes__tag__name')
    for art in articles_list:
        for scope in art.scopes.all().order_by('tag__name'):
            print(scope.tag.name)

    context = {
        'object_list': articles_list,
    }
    return render(request, template, context)
