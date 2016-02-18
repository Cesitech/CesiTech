from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from blog.models import *
from blog.forms import *
#-*- coding: utf-8 -*-

def home(request):
    AllProject = Project.objects.all()
    team = Membre.objects.filter(rang=10).values()
    calendar = Calendar.objects.order_by('date')
    news = New.objects.order_by('-date')
    if news.count()>4 :
        calendar = calendar[4]
    totalNew = news.count()
    news_first = news[0]
    news = news[1:]

    if calendar.count()>4:
        index = 0
        for c in calendar:
            if c.date.isoformat() > timezone.now().isoformat() :
                if index + 4 > calendar.count():
                    index = calendar.count()-4
                calendar = calendar[index:index+4]
                break;
            index += 1

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

    return render(request, 'cesitech/index.html', locals())

def project(request, ide):
    AllProject = Project.objects.all()
    project = get_object_or_404(Project, id=ide)
    team = Membre.objects.filter(team_id=project.team).values()
    calendar = Calendar.objects.filter(projet_id=ide).order_by('date')

    if calendar.count()>4:
        index = 0
        for c in calendar:
            if c.date.isoformat() > timezone.now().isoformat() :
                if index + 4 > calendar.count():
                    index = calendar.count()-4
                calendar = calendar[index:index+4]
                break;
            index += 1

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

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
