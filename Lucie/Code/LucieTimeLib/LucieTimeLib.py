#!/usr/bin/env/python
# -*- coding:Utf-8 -*-

"""

LucieTimeLib .. > Main.py

Librairie des éléments temporels du robot "Lucie". Permet de connaitre l'heure et d'effectuer des opérations avec.


=== STICKYNOTES =====================


!!!!!!!!!! ATTENTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                              !! --> D'ailleurs il faudrait écrire une fonction qui
!! L'heure de référence est celle du système!   !!     mette à l'heure le système dans ce fichier, si
!! Il faut donc que le système soit à l'heure!  !!     quelqu'un s'en sent.. Moi je ne connais pas les API d'horloge.
!! ça éviterait de raconter n'importe quoi...   !!                    -- Guillaume
!!                               ;)             !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




=== CHANGELOG ===================


DATE       CONTRIBUTEUR              NOTES
================================================================================================================
23/01/16   Guillaume TORREILLES       - Création du script
                                      - Création des fonctions : __init__,
                                                                 get_date_time,
                                                                 time_natural_language,
                                                                 date_natural_language,
                                                                 date_and_time_natural_language.
-----------------------------------------------------------------------------------------------------------------


"""

import datetime

mois  = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
jours = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

def __init__():
    global mois,jours
    # Creer les listes globales
    mois  = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
    jours = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

def get_date_time():
    return str(datetime.datetime.now())

def time_natural_language():
    a = ((get_date_time().split(" ")[1]).split(".")[0]).split(":")
    #print "il est "+str(a[0])+" heures, "+str(a[1])+" minutes et "+str(a[2])+" secondes."
    return "il est "+str(a[0])+" heures, "+str(a[1])+" minutes et "+str(a[2])+" secondes." # On se moque de l'orthographe! c'est phonétique

def time_natural_language_short():
    a = ((get_date_time().split(" ")[1]).split(".")[0]).split(":")
    #print "il est "+str(a[0])+" heures, "+str(a[1])+" minutes et "+str(a[2])+" secondes."
    return "il est "+str(a[0])+" heures "+str(a[1])+"."


def date_natural_language():
    global mois,jours
    a = (get_date_time().split(" ")[0]).split("-")
    #print("Nous sommes le "+str(a[2])+" "+str(mois[int(a[1])-1])+" "+str(a[0])+". Et je m'excuse, mais je ne sais pas déterminer quel jour de la semaine nous sommes. C'est ça de faire tourner un logiciel béta!")
    return "Nous sommes le " + jours[datetime.datetime.today().weekday()] + " " + str(a[2])+" "+str(mois[int(a[1])-1])+" "+str(a[0])+"."

def date_and_time_natural_language():
    return date_natural_language() + " et " + time_natural_language_short()


def day_natural_language():
    return "Nous sommes " + jours[datetime.datetime.today().weekday()]

def test_lib():
    """
    Tester la librairie.
    Personnaliser la fonction pour tester des éléments en particuliers.
    """
    print "time_natural_language()"
    print time_natural_language()
    
    print("\n")
    
    print "date_and_time_natural_language()"
    print date_and_time_natural_language()
    
    print("\n")
    
    print "time_natural_language_short()"
    print time_natural_language_short()
    
    print("\n")
    
    print "date_natural_language()"
    print date_natural_language()
    
    print("\n")
    
    print "day_natural_language()"
    print day_natural_language()


###  T E S T  ###

# Commenter pour désactiver le mode test

test_lib()