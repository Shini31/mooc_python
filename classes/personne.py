# Definition de la classe Personne
class Personne:
    """Classe definissant une personne caracterisee par :
    - son nom
    - son prenom
    - son age
    - son lieu de residence"""

# Constructeur
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.age = 34
        self.residence = "L'union"
