from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    contenu = models.TextField(null=False, verbose_name="Contenu")
    auteur = models.ForeignKey('Membre')
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de creation")
    categorie = models.ForeignKey('Categorie')
    def __str__(self):
        return self.titre

    def __unicode__(self):
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom
    def __unicode__(self):
        return self.nom

class New(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    image = models.CharField(max_length=255, verbose_name="Image")
    contenu = models.TextField(null=False, verbose_name="Contenu")
    categorie = models.ForeignKey('Categorie')
    auteur = models.ForeignKey('Membre')
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    def __str__(self):
        return self.titre
    def __unicode__(self):
        return self.titre

class Membre(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prenom")
    mail = models.CharField(max_length=155, verbose_name="mail")
    password = models.CharField(max_length=100, verbose_name="Mot de Passe")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de creation")
    rang = models.ForeignKey('Rang')
    def __str__(self):
        return self.prenom
    def __unicode__(self):
        return self.prenom

class Rang(models.Model):
    rang = models.CharField(max_length=100, verbose_name="Rang")
    def __str__(self):
        return self.rang
    def __unicode__(self):
        return self.rang

class Contact(models.Model):
    sujet = models.CharField(max_length=100, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    envoyeur = models.CharField(max_length=100, verbose_name="Envoyeur")
    renvoi = models.BooleanField(verbose_name="Avoir un retour")
    date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Date d'envoie")
    def __str__(self):
        return self.sujet
    def __unicode__(self):
        return self.sujet
