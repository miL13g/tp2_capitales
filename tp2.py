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
from utilitaires import lire_entier, lire_reel, lire_texte, lire_oui_non, normaliser
from donnees_tp2 import PAYS, CAPITALES_PAYS, PROVINCES, CAPITALES_PROVINCES, ETATS, CAPITALES_ETATS

init(autoreset=True)

######################################################

######################################################
#Constantes
liste_standard= []   
liste_standard_capitales = []
liste_aventure = []
liste_aventure_reponse = []
lieux_rates = []
reponse_donnees = []
capitales_rates = []
liste_niveaux = ["Facile","Normal","Avancé"]
#liste_questions = [5,10,15] # pas utilisé?
liste_modes = ["Standard","Aventure"]

######################################################

######################################################
#Variables

######################################################
######################################################
#Fonctions
def demander_nom():# à documenter
    nom = input(f"Quel est ton nom jeune bambin? : ")
    return nom


def afficher_menu(titre, options,texte):
    """Affiche le menu selon l'option. 

    Args:
        titre (str): Le message affiché à l'utilisateur.
        options (list): la liste de l'option désiré.

    Returns:
        int: Le nombre saisi.
    """
    print(titre)
    for i in range(len(options)):
            print(f"{i+1} - {options[i]} {texte[i]}")
    valeur = lire_entier("Votre choix : ",1, len(options))
    return valeur

def afficher_mode():
    """Demande le mode désiré par le joueur

    Returns:
        int: Le choix du mode du joueur
    """
    texte_mode = ["(196 pays du monde)","(259 lieux : pays + provinces et territoires du Canada + États américains)"]
    choix = afficher_menu("MODE DE JEU",liste_modes,texte_mode)
    return choix


def afficher_niveau():
    """Demande le niveau désiré par le joueur 

    Returns:
        int: Le choix du niveau du joueur
    """
    texte_question = ["(5 questions)","(10 questions)","(15 questions)"]
    choix = afficher_menu("NIVEAU DE DIFFICULTÉ",liste_niveaux,texte_question)
    return choix


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


def est_bonne_reponse(reponse, capitale):# à vérifier si le in est un tableau qui vérifie un tableau ou peut être un str qui vérifie dans un tableau
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


def calculer_pourcentage(nb_bonnes, nb_questions): #utilise la variable du pointage de questions réussies en relation avec le nombre de questions totales
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

def afficher_bilan(message,pourcentage):
    """Affiche le bilan du pointage de la partie ainsi que l'appréciation selon le pourcentage.

    Args:
        message (str): Message à afficher en fin de partie
        pourcentage (int): Le pourcentage de bonne réponse de la partie
    """
    print("*"*78)
    print(message)
    print(obtenir_appretiation(pourcentage))
    print("*"*78)



def jouer_partie(lieux, capitales, nb_questions, nom):# à documenter
    
    NB_QUESTIONS = [5, 10, 15]

    nb_questions = NB_QUESTIONS[nb_questions - 1] 

    liste_valeurs_aleatoires = random.sample(range(0, len(lieux)), nb_questions)

    lieux_rates = []
    capitales_rates = []
    reponses_rates = []

    nb_bonnes = 0

    for i in range (len(liste_valeurs_aleatoires)):
        index_question = liste_valeurs_aleatoires[i]
        print(f"Question {i + 1} de {nb_questions} - {lieux[index_question]}")
        valide = False
        while not valide:
            try:
                question = lieux[index_question]
                capitale = capitales[index_question]
                capitale = normaliser(capitale)
                reponse = lire_texte("Capitale : ")
                reponse = normaliser(reponse)
                if est_bonne_reponse(reponse, capitale) == True:
                    nb_bonnes += 1
                    print(Fore.GREEN + f"Bonne réponse! Pointage {nb_bonnes}/{i+1}")
                    valide = True
                else:
                    print (Fore.RED + f"Mauvaise réponse! On cherchait : {capitales[index_question]}. Pointage : {nb_bonnes} / {i+1}")
                    lieux_rates.append(question)
                    capitales_rates.append(capitale)
                    reponses_rates.append(reponse)
                    valide = True
            except:
                print("yooo")

    # Créer le bilan ici!!! #


    return lieux_rates, capitales_rates, reponses_rates, nb_bonnes, nb_questions

                

def afficher_revision(lieux_rates, reponses_donnees, capitales_rates):
    """Affiche un tableau de révision selon les fautes commises

    Args:
        lieux_rates (list): Liste du nom des lieux ratés
        reponses_donnees (list): liste des mauviases réponses données par l'utilisateur
        capitales_rates (list): liste des capitales des lieux ratés
    """
    print(f"{"À RÉVISER":^78}")
    print("-"*78)
    print(f"{"Lieu":<32}| {"Votre réponse ":<15}| {"Bonne réponses":<25}")
    print("-"*78)
    if reponses_donnees == []:
        print(Fore. GREEN + f"Aucune erreur : rien à réviser!" + Style.RESET_ALL)
    else :
        for i in range(len(reponses_donnees)):
            print(f"{lieux_rates[i]:<32}| {reponses_donnees[i]:<15.15}| {capitales_rates[i]:<25}")
    print("-"*78)        
    
    # HISTORIQUE ICI #


######################################################

######################################################
#Fonction Main()
def main():
    afficher_bienvenue()
    nom = demander_nom()
    print(f"Salut {nom}")
    rejouer = True #à réviser l'emplacement
    valide = False
    while not valide:
        if not rejouer:
            valide = True
        else:
            valeur_mode = afficher_mode()
            liste_questions = construire_listes(valeur_mode)
            liste_lieux = liste_questions[0]
            liste_capitales = liste_questions[1]
            valeur_niveau = afficher_niveau()
            score = jouer_partie(liste_lieux, liste_capitales, valeur_niveau, nom)
            lieux_rates = score[0]
            capitales_rates = score[1]
            reponse_donnees = score[2]
            reponse_bonnes = score[3]
            nombre_questions = score[4]
            pourcentage = calculer_pourcentage(reponse_bonnes,nombre_questions)
            afficher_bilan(f"{nom}, votre pointage est de {reponse_bonnes} sur {nombre_questions} ({pourcentage} %).",pourcentage)
            afficher_revision(lieux_rates, reponse_donnees, capitales_rates)
            rejouer = lire_oui_non("Voulez-vous rejouer? (o/n) : ")
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