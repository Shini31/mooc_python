# Definition de la classe TableauNoir
class TableauNoir:
    """Classe définissant un tableau noir où l'on peut:
    - écrire
    - lire
    - effacer"""

# Constructeur
    def __init__(self):
        """Surface vide"""
        self.surface()

    def ecrire(self, texte):
        """Permet d'écrire sur le tableau noir
        avec un retour de ligne"""
        if self.surface != "":
            self.surface += "\n"
        self.surface += texte

    def lire(self):
        """Permet de lire le tableau"""
        print(self.surface)

    def effacer(self):
        """PErmet d'effacer le tableau noir"""
        self.surface = ""
