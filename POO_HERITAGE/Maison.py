from Batiment import *

class Maison(Batiment):
    # definition des paramètres utilisés dans le constructeur de la classe Maison
    def __init__(self, adress:str, surface:int, nb_piece:int, surface_jardin:int):
        # execution du constructeur de la classe mère
        super().__init__(adress, surface)
        # definition et initialisaiton des attributs de la classe Maison
        self.nb_piece = nb_piece
        self.surface_jardin = surface_jardin

    # polymorphisme : ici pour un même nom de méthode en fonction de la classe ca fait des choses différentes
    def __str__(self):
        return super().__str__() + " , Nombre de pièces : " + str(self.nb_piece) + " , Surface de jardin: " + str(self.surface_jardin)
