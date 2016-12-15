# -*- coding: utf-8 -*-

"""Fonctions pour le jeu du pendu"""

import os
import pickle
from random import choice

from donnees import *


# Recuperation du nom du joueur
def recup_user():
    pseudo = input("Saisissez votre pseudo: ")
    pseudo = pseudo.capitalize()

    if not pseudo.isalnum() or len(pseudo)<4:
        print("Ce pseudo est invalide.")
        return recup_user()
    else:
        return pseudo

# Récupération du score
def recup_score():
    if os.path.exists(fichier_scores):
        with open('fichier_scores', 'rb') as fichier:
            score_depickler = pickle.Unpickler(fichier)
            score = score_depickler.load()
    else:
        score = {}
    return score

# Sauvegarde du score
def ecrire_score(score):
    with open('fichier_scores', 'wb') as fichier:
        score_pickler = pickle.Pickler(fichier)
        score_pickler = score_pickler.dump(score)

# Choix aléatoire du mot dans la liste
def choix_mot():
    return choice(liste_mots)

# Comparaison lettres trouvées et mot
def recup_mot_masque(mot_complet, lettres):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque

# Récupération de la lettre
def recup_lettre():
    lettre = input("Saisissez une lettre: ")
    lettre = lettre.lower()

    if len(lettre) > 1 or not lettre.isalpha():
        print("Cette lettre est invalide.")
        return recup_lettre()
    else:
        return lettre
