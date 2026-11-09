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
liste_standard= []   #est-ce correcte de mettre les listes dans les constantes?
liste_standard_capitales = []
liste_aventure = []
liste_aventure_reponse = []
lieux_rates = []
reponse_donnees = []
capitales_rates = []
liste_niveaux = ["Facile","Normal","Avancé"]
liste_questions = [5,10,15]
liste_modes = ["Standard","Aventure"]
liste_options_modes = []
liste_options_niveaux = []

######################################################

######################################################
#Variables

######################################################
######################################################
#Fonctions
def demander_nom():# à documenter
    nom = input(f"Quel est ton nom jeune bambin? : ")
    return nom

def construire_option(liste):
    """construit la liste d'options selon l'option choisie

    Args:
        liste (list): La liste d'options désiré

    Returns:
        list: Une liste de texte à l'index +1 des modes 
    """
    option_courante=[]
    for i in range(len(liste)):
        liste_courante = f"{i+1} - {liste[i]}"
        option_courante.append(liste_courante)
    return option_courante


def afficher_menu(titre, options):
    """Affiche le menu selon l'option. 

    Args:
        titre (str): Le message affiché à l'utilisateur.
        options (list): la liste de l'option désiré.

    Returns:
        int: Le nombre saisi.
    """
    print(titre)
    texte_mode = ["(196 pays du monde)","(259 lieux : pays + provinces et territoires du Canada + États américains)"]
    texte_question = ["(5 questions)","(10 questions)","(15 questions)"]
    if options == liste_options_modes:
        for i in range(len(options)):
            print(f"{options[i]} {texte_mode[i]}")
    if options == liste_options_niveaux:
        for i in range(len(options)):
            print(f"{options[i]} {texte_question[i]}")
    valeur = lire_entier("Votre choix : ",1, len(options))
    return valeur


def afficher_bienvenue():# à documenter
    print(f"+{'-'*76}+")
    print(f"|{"Jeu questionnaire - Les Capitales":^76}|")
    print(f"|{"réalisé par Francis et Émile":^76}|")
    print(f"+{'-'*76}+")


def construire_listes(mode):# à documenter
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


def est_bonne_reponse(reponse, capitale):# à vérifier si le in est un tableau qui vérifie un tableau ou peut être un str qui vérifie dnas un tableau
    """Vérifie sur la réponse est bonne ou mauvaise

    Args:
        reponse (str): réponse inscrite par le joueur
        capitale (str): La réponse à valider

    Returns:
        bool: Si la réponse est bonne ou mauvaise.
    """
    tableau_capitales = capitale.split("/")
    for i in range(len(tableau_capitales)):
        if(tableau_capitales[i] == reponse):
            return True
    return False


def calculer_pourcentage(nb_bonnes, nb_questions):# à documenter et ajouter return
    pourcentage = (nb_bonnes * 100) // nb_questions
    return pourcentage

def obtenir_appretiation(pourcentage):
    """Donne l'appréciation en fonction du pourcentage obtenu.

    Args:
        pourcentage (int): Pourcentage obtenu par l'utilisateur

    Returns:
        str: L'appréciation
    """
    match pourcentage:
        case 100:
            return "Parfait! Un vrai globe-trotter!"
        case _ if pourcentage >= 80:
            return "Excellent!"
        case _ if pourcentage >= 60:
            return "Bon Travail!"
        case _ if pourcentage >= 40:
            return "Pas mal, mais l'atlas pourrait vous aider."
        case _ if pourcentage < 40:
            return "Il est temps de sortir l'atlas!"
        case _ :
            return "Pourcentage invalide."


def jouer_partie(lieux, capitales, nb_questions, nom):# à documenter

    if nb_questions == 1:
        nb_questions = 5
    elif nb_questions == 2:
        nb_questions = 10
    elif nb_questions == 3:
        nb_questions = 15
    else:
        print("How bruva")


    for i in range (nb_questions):
        nb_bonnes = 0
        pays_demande = random.randrange(1,len(lieux))
        capitale = pays_demande[i]
        print(f"Question {i + 1} de {nb_questions} - {pays_demande}")
        valide = False
        while not valide:
            try:
                pays_demande = random.randrange(1,len(lieux))
                print(pays_demande)
                reponse = lire_texte("Quel est la Capitale???????????? : ")
                if est_bonne_reponse(reponse, pays_demande) == True:
                    nb_bonnes += 1
                    print(f"Bonne réponse! Pointage {nb_bonnes}/{nb_questions}")
                else:

                    print ("Mauvaise réponse! On cherchait : ")

            except:
                print("yooo")
                

def afficher_revision(lieux_rates, reponses_donnees, capitales_rates):
    print(f"{"À RÉVISER":^78}")
    print("-"*78)
    print(f"{"Lieu":<32}| {"Votre réponse ":<15}| {"Bonne réponses":<25}")
    print("-"*78)
    if reponses_donnees == 0:
        print(Fore. GREEN + f"Aucune erreur : rien à réviser!" + Style.RESET_ALL)
    else :
        for i in range(reponses_donnees):
            print(f"{lieux_rates[i]:<32}| {reponses_donnees[i]:<15}| {capitales_rates[i]:<25}")
    print("-"*78)        
    
afficher_revision(0,0,0)



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
    afficher_bienvenue()
    nom = demander_nom()
    print(f"Salut {nom}")
    rejouer = "" #à réviser l'emplacement
    valide = False
    while not valide:
        if rejouer == "n":
            valide = True
        else:
            liste_options_modes = construire_option(liste_modes)
            valeur_mode = afficher_menu("MODE DE JEU",liste_options_modes)
            print(valeur_mode)
            construire_listes(valeur_mode)
            liste_options_niveaux = construire_option(liste_niveaux)
            valeur_niveau = afficher_menu("NIVEAU DE DIFFICULTÉ",liste_options_niveaux)
            print(valeur_niveau)
            jouer_partie(PAYS, CAPITALES_PAYS, valeur_niveau, nom)
            #rejouer = demander oui_non
    #afficher_historique()
######################################################

######################################################
#Appel main()

main()
######################################################


########## POUR CE SOIR ##########
# - fonction jouer_partie (meat'n potatoes)
#  - comprendre la méthode et la bonnne utilisation de random
#   - la fonction random devra être utilisé pour aller piger 
#     dans la/les liste(s) de lieux dans une boucle "for i in range"
# - après ça on vera pcq clairement on peut prendre la nuite la d'ssus
##################################