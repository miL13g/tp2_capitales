"""Fonctions utilitaires de saisie validée et de traitement de texte.

Module de départ du TP2 : il reprend tel quel le fichier utilitaires.py du
Cours 07 (Café Le Binaire). Vous devez le compléter selon l'énoncé.

Auteur(s) : __________ et __________
Date      : __________
"""

# ---------------------------------------------------------------------------
# À FAIRE (voir l'énoncé, section « Fonctions obligatoires ») :
#   1. Afficher EN ROUGE les messages d'erreur de lire_entier() et de
#      lire_oui_non() (module colorama).
#   2. Ajouter la fonction lire_texte(message).
#   3. Ajouter la fonction normaliser(texte).
#   4. Documenter les nouvelles fonctions (docstring au format Google).
# ---------------------------------------------------------------------------

##############################
#import
from colorama import Fore, Style
##############################

def lire_entier(message, minimum=0, maximum=99):
    """Demande un nombre entier jusqu'à ce que la saisie soit valide.

    Args:
        message (str): Le message affiché à l'utilisateur.
        minimum (int, optional): La plus petite valeur acceptée. Par défaut 0.
        maximum (int, optional): La plus grande valeur acceptée. Par défaut 99.

    Returns:
        int: L'entier saisi, compris entre minimum et maximum.
    """
    valide = False
    while not valide:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                print(Fore.RED+ f"Erreur : entrez un nombre entre {minimum} et {maximum}."+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + f"Erreur : ce n'est pas un nombre entier."+ Style.RESET_ALL)
    return valeur

def lire_reel(message, minimum=0.0):
    """Demande un nombre réel jusqu'à ce que la saisie soit valide.

    Args:
        message (str): Le message affiché à l'utilisateur.
        minimum (float, optional): La plus petite valeur acceptée. Par défaut 0.0.

    Returns:
        float: Le nombre saisi, supérieur ou égal à minimum.
    """
    valide = False
    while not valide:
        try:
            valeur = float(input(message))
            if valeur >= minimum:
                valide = True
            else:
                print(f"Erreur : entrez un nombre supérieur ou égal à {minimum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre valide.")
    return valeur


def lire_oui_non(message):
    """Pose une question fermée jusqu'à obtenir « o » ou « n ».

    Args:
        message (str): La question affichée à l'utilisateur.

    Returns:
        bool: True si l'utilisateur répond « o », False s'il répond « n ».
    """
    reponses_valides = ("o", "n")
    reponse = input(message).strip().lower()
    while reponse not in reponses_valides:
        print(Fore.RED + "Erreur : répondez par o ou n." + Style.RESET_ALL)
        reponse = input(message).strip().lower()
    return reponse == "o"

def lire_texte(message):
    nom = input(message).strip()
    while nom == "":
        print("Le nom ne peut pas être vide.")
        nom = input(message).strip()
    return nom


# def normaliser(texte):

# Tests rapides : exécutés seulement si on lance ce fichier directement,
# jamais lorsqu'il est importé par un autre fichier.
if __name__ == "__main__":
    age = lire_entier("Âge (0 à 120) : ", 0, 120)
    print("Entier lu :", age)
    montant = lire_reel("Montant : ")
    print("Réel lu :", montant)
    print("Réponse :", lire_oui_non("Continuer? (o/n) : "))
    # À FAIRE : ajouter ici quelques tests de lire_texte() et de normaliser()
