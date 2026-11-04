"""
Sujet : Code prncipal du programme Tp2 Jeu questionnaire sur les capitales.
Auteur(s) : Francis St-Cyr et Émile Bousquet
Date      : 03 novembre 2026
"""

######################################################
#Import

import random
random.seed(10)
from colorama import Fore, Style
from utilitaires import lire_entier, lire_reel, lire_texte, lire_oui_non
from donnees_tp2 import PAYS, CAPITALES_PAYS, PROVINCES, CAPITALES_PROVINCES, ETATS, CAPITALES_ETATS

######################################################

######################################################
#Constantes

######################################################

######################################################
#Fonctions
def afficher_menu(titre, options):
    """Affiche le menu selon l'option. 

    Args:
        titre (str): Le message affiché à l'utilisateur.
        options (int): Choix de menu (2 ou 3)

    Returns:
        int: Le nombre saisi.
    """
    print(titre)
    if options == 2:
        print("1 - Standard (196 pays du monde)")
        print("2 - Standard (259 lieux : pays + provinces et territoires du Canada + États américains)")
    # for i in range(options):
    #     print(f"{i+1} - ")
    elif options == 3:
        print("1 - Facile (5 questions)")
        print("2 - Normal (10 questions)")
        print("3 - Avancé (15 questions)")
    valeur = lire_entier("Votre choix : ",1, options)
    return valeur

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




# liste_noms = ["Brouillette", "Adam" "Frenette", "Alie"]
# liste_prenoms ["David", "Benoit", "Nicole", "Robert"]

#valeur_index = random.randrange(1,len(liste_noms))

#print(liste_noms, liste_prenoms)
#print(f"Mon index random est: {valeur_index}")
#print(f"Le nom est {liste_noms[valeur_index]} et le prénom est {liste_prenoms[valeur_index]}")
######################################################

######################################################
#Fonction Main()
valeur_mode = afficher_menu("MODE DE JEU", 2)
print(valeur_mode)
valeur_niveau = afficher_menu("NIVEAU DE DIFFICULTÉ", 3)
print(valeur_niveau)
######################################################

######################################################
#Appel main()
afficher_bienvenue()
construire_listes(valeur_mode)
print("fin")
######################################################