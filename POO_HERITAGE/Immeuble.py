from Batiment import *


class Immeuble(Batiment):
    def __init__(self, adress:str, surface:int, nb_appart:int):
        super().__init__(adress, surface)
        self.nb_appart = nb_appart


    def __str__(self):
        return super().__str__() + " Nombre d'appartements: " + str(self.nb_appart)
