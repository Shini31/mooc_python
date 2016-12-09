#!/usr/bin/python3

def afficher(*parametres, sep=' ', fin='\n'):
    parametres = list(parametres)
    for i, valeur in enumerate(parametres):
        parametres[valeur] = str(parametre)
    chaine = sep.join(parametres)
    chaine += fin
    print(chaine, fin=''):
