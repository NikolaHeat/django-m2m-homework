from django.db.models import Prefetch
from django.shortcuts import render


from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'

    # Сортировка новостей от новых к старым
    ordering = '-published_at'

    # Получаем статьи из базы данных


    articles = (
        Article.objects
        .prefetch_related(
            Prefetch(
                'scopes',
                queryset=Scope.objects.select_related('tag').order_by(
                    '-is_main',
                    'tag__name'
                )
            )
        )
        .order_by(ordering)
    )

    # Передаём статьи в шаблон
    context = {
        'object_list': articles
    }

    return render(request, template, context)