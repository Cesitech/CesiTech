from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from blog.models import Article
#-*- coding: utf-8 -*-

def home(request):
    article = Article.objects.all()
    return render(request, 'blog/index.html', {'date':datetime.now(), 'dernier_articles':article})

def view_article(request, id_article):
    text = """Vous avez demande l'article #{0}!""".format(id_article)
    return HttpResponse(text)
