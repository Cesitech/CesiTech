from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import *
from blog.forms import ContactForm
#-*- coding: utf-8 -*-

def admin(request):
    return render(request, 'cesitech/admin.html', {'date':datetime.now()})

def home(request):
    article = Article.objects.all()
    return render(request, 'cesitech/index.html', {'date':datetime.now(), 'dernier_articles':article})

def view_article(request, id_article):
    article = get_object_or_404(Article, id=id_article)
    return render(request, 'cesitech/lire.html', {'date':datetime.now(), 'article':article})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            form.save()
            envoi = True
    form = ContactForm()

    return render(request, 'cesitech/contact.html', locals())
