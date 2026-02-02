from Animal import *
from typing import List

class Enclos:
    def __init__(self, taille_max:int, name:str):
        self.taille_max = taille_max
        self.list_animaux:List[Animal] = []
        self.name = name

    def get_nb_animaux(self)->int:
        return len(self.list_animaux)

    def est_plein(self)->bool:
        return len(self.list_animaux) == self.taille_max

    def feed_all(self)->None:
        for animal in self.list_animaux:
            if animal.faim >= 5:
                animal.nourrir()

    def ajoute(self, a:Animal)->bool:
        if not self.est_plein():
            for animal in self.list_animaux:
                if not a.compatibilite(animal):
                    return False
            self.list_animaux.append(a)
            return True
        return False

    def description(self)->None:
        print("\nNom de l'enclos", self.name)
        for animal in self.list_animaux:
            print(animal.description())

    def reproduction(self)->None:
        for animal in self.list_animaux:
            animal.is_reproduced = False
        for animal_1 in self.list_animaux:
            if not animal_1.is_reproduced and not self.est_plein():
                print("tentative de reproduction de animal 1", animal_1.description())
                for animal_2 in self.list_animaux:
                    if not animal_2.is_reproduced:
                        baby = animal_1.reproduction(animal_2)
                        if baby:
                            print("Naissance de :", baby.description())
                            self.list_animaux.append(baby)
                            animal_1.is_reproduced = True
                            animal_2.is_reproduced = True
                            break
                        else:
                            print("Echec")
