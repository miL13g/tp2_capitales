"""
Sujet : Code prncipal du programme Tp2 Jeu questionnaire sur les capitales.
Auteur(s) : Francis St-Cyr et Émile Bousquet
Date      : 03 novembre 2026
"""

######################################################
#Import

import random
random.seed(10)
from colorama import Fore, Style, init
from utilitaires import lire_entier, lire_reel, lire_texte, lire_oui_non
from donnees_tp2 import PAYS, CAPITALES_PAYS, PROVINCES, CAPITALES_PROVINCES, ETATS, CAPITALES_ETATS

init()

######################################################

######################################################
#Constantes

######################################################

######################################################
#Variables
liste_standard= []
liste_standard_reponse = []
liste_aventure = []
liste_aventure_reponse = []
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
    if mode == 1:
        return PAYS, CAPITALES_PAYS
    elif mode == 2:
        liste_aventure = PAYS + PROVINCES + ETATS
        liste_aventure_reponse = CAPITALES_PAYS + CAPITALES_PROVINCES + CAPITALES_ETATS
        return liste_aventure, liste_aventure_reponse

liste_retour = construire_listes(1)
liste_standard = liste_retour[0]
liste_standard_reponse = liste_retour[1]

liste_retour = construire_listes(2)
liste_aventure = liste_retour[0]
liste_aventure_reponse = liste_retour[1]


def est_bonne_reponse(reponse, capitale):
    print("yo")



def calculer_pourcentage(nb_bonnes, nb_questions):
    pourcentage = (nb_bonnes * 100) // nb_questions


# def jouer_partie(lieux, capitales, nb_questions, nom):
#     for i in range (len(nb_questions)):
#         print(f"Question {i + 1} de {nb_questions} - {lieu}")
#         valide = False
#         while not valide:
#             try:
#                 capitale = input(f"Capitale : ")
                
        



# liste_noms = ["Brouillette", "Adam" "Frenette", "Alie"]
# liste_prenoms ["David", "Benoit", "Nicole", "Robert"]

#valeur_index = random.randrange(1,len(liste_noms))

#print(liste_noms, liste_prenoms)
#print(f"Mon index random est: {valeur_index}")
#print(f"Le nom est {liste_noms[valeur_index]} et le prénom est {liste_prenoms[valeur_index]}")
######################################################

######################################################
#Fonction Main()
def main():
    valeur_mode = afficher_menu("MODE DE JEU", 2)
    print(valeur_mode)
    construire_listes(valeur_mode)
    valeur_niveau = afficher_menu("NIVEAU DE DIFFICULTÉ", 3)
    print(valeur_niveau)
######################################################

######################################################
#Appel main()

afficher_bienvenue()
main()
print("fin")
######################################################