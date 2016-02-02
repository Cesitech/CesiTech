from django.http import HttpResponse
from django.shortcuts import render

#-*- coding: utf-8 -*-

def home(request):
    return render(request, 'blog/date.html', {'date':datetime:now()})

def view_article(request, id_article):
    text = """Vous avez demande l'article #{0}!""".format(id_article)
    return HttpResponse(text)
