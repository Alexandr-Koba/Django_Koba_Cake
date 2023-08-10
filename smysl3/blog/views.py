from django.shortcuts import render
from .models import Article

def home_page(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home_page.html', context)

def article_page(request, article_id):
    article = Article.objects.get(pk=article_id) #загружает 1 обьект из таблицы Articles по id
    context = {'article': article}
    return render(request, 'article_page.html', context) # поподаю в шаблон