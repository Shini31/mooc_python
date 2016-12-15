#!/usr/bin/python3
# -*- coding: utf-8 -*-

from donnees import *
from fonctions import *

scores = recup_score()

user = recup_user()

if user not in scores.keys():
    scores[user] = 0

continuer_partie = "o"

while continuer_partie != 'n':
    print("Joueur {0}: {1} point(s)".format(user, scores[user]))
    mot_a_trouver = choix_mot()

    lettres_trouvees = []

    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    nb_chances = nb_coups

    while mot_a_trouver != mot_trouve and nb_chances > 0:
        print("Mot à trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees:
            print("Vous avez déjà trouvé cette lettre")
        elif lettre in mot_a_trouver:
            print("Bravo ! Vous avez la lettre {0}".format(lettre))
            lettres_trouvees.append(lettre)
        else:
            print("Désolé la lettre {0} ne fait partie du mot".format(lettre))
            nb_chances -= 1
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    if mot_trouve == mot_a_trouver:
        print("Félicitations, vous avez trouvé le mot {0} !!!".format(mot_a_trouver))
    else:
        print("Désolé, vous avez perdu...")

    scores[utilisateur] += nb_chances

    continuer_partie = input("Souhaitez-vous continuer la partie (O/N) ?")
    continuer_partie = continuer_partie.lower()

enregistrer_scores(scores)

print("Vous finissez la partie avec {0} points.".format(scores[utilisateur]))
