from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class New(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    avatar = models.ImageField(blank=True, upload_to="static/images/")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    contenu = models.TextField(verbose_name="Contenu")
    auteur = models.ForeignKey('Membre')
    def __str__(self):
        return self.titre
    def __unicode__(self):
        return self.titre

class Membre(models.Model):
    user = models.OneToOneField(User)
    fonction = models.CharField(max_length=50, verbose_name="Fonction")
    avatar = models.ImageField(blank=True, upload_to="static/avatars/")
    description = models.CharField(max_length=155, verbose_name="Description")
    rang = models.CharField(max_length=4, verbose_name="Rang")
    team = models.ForeignKey('Team')
    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username

class Contact(models.Model):
    sujet = models.CharField(max_length=100, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    envoyeur = models.CharField(max_length=100, verbose_name="Envoyeur")
    date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Date d'envoie")
    def __str__(self):
        return self.sujet
    def __unicode__(self):
        return self.sujet

class Project(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom du projet")
    description = models.TextField(verbose_name="Description")
    team = models.ForeignKey('Team')
    date_modifcation = models.DateTimeField(auto_now_add=True, verbose_name="Date modification")
    def __str__(self):
        return self.nom
    def __unicode__(self):
        return self.nom

class Team(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom de l'equipe")
    permission = models.CharField(max_length=100, verbose_name="Permission")
    def __str__(self):
        return self.nom
    def __unicode__(self):
        return self.nom

class Calendar(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de l'evenement")
    date = models.DateTimeField(verbose_name="Date de l'evenement")
    description = models.TextField(verbose_name="Description de l'evenement")
    projet_id = models.ForeignKey('Project')
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
