from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import *
from blog.forms import ContactForm
#-*- coding: utf-8 -*-

def home(request):
    allProject = Project.objects.all()
    team = Membre.objects.filter(team_id=1).values()

    envoi = False
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

    return render(request, 'cesitech/index.html', {'typeView':'Project', 'AllProject':allProject, 'team':team, 'contact':form, 'envoi':envoi})

def project(request, ide):
    AllProject = Project.objects.all()
    project = get_object_or_404(Project, id=ide)
    team = Membre.objects.filter(team_id=project.team).values()

    envoi = False
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

    return render(request, 'cesitech/project.html', locals())

def article(request):
    article = Article.objects.all()
    return render(request, 'cesitech/index.html', {'dernier_articles':article, 'typeView':'ArticleAll'})

def view_article(request, id_article):
    article = get_object_or_404(Article, id=id_article)
    return render(request, 'cesitech/lire.html', {'article':article, 'typeView':'ArticleID'})
