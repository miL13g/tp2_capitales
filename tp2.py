"""
Sujet : Code prncipal du programme Tp2 Jeu questionnaire sur les capitales.
Auteur(s) : Francis St-Cyr et Émile Bousquet
Date      : 03 novembre 2026
"""

######################################################
#Import

import math

import random

from colorama import Back, Fore, Style, init

from donnees_tp2 import PAYS, CAPITALES_PAYS, PROVINCES, CAPITALES_PROVINCES, ETATS, CAPITALES_ETATS

init()

######################################################

######################################################
#Constantes

######################################################

######################################################
#Fonctions

def afficher_bienvenue():
    print(f"+{'-'*76}+")
    print(f"|{"Jeu questionnaire - Les Capitales":^76}|")
    print(f"|{"réalisé par Francis et Émile":^76}|")
    print(f"+{'-'*76}+")


def construire_listes(mode):
    liste_pays= []
    liste_capitales_pays = []
    liste_provinces = []
    liste_capitales_provinces = []
    liste_etats = []
    liste_capitales_etats = []
    if mode == 1:
        liste_pays.append(PAYS)
        liste_capitales_pays.append(CAPITALES_PAYS)
    elif mode == 2:
         liste_pays.append(PAYS)
         liste_capitales_pays.append(CAPITALES_PAYS)
         liste_provinces.append(PROVINCES)
         liste_capitales_provinces.append(CAPITALES_PROVINCES)
         liste_etats.append(ETATS)
         liste_capitales_etats.append(CAPITALES_ETATS)


def calculer_pourcentage(nb_bonnes, nb_questions):
    pourcentage = nb





######################################################

######################################################
#Fonction Main()

######################################################

######################################################
#Appel main()
afficher_bienvenue()
construire_listes(valeur_mode)
print("fin")
######################################################