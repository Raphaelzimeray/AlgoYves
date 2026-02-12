from Enclos import *
from typing import List

class Zoo:
    def __init__(self, city:str, content:List[Enclos]):
        self.city = city
        self.content = content

    def add_animal_in_zoo(self, a:Animal)->bool:
        for enclos in self.content:
            if not enclos.est_plein():
                enclos.ajoute(a)
                return True
        return False

    def plus_vieux(self)->Animal:
        age_max = 0
        oldest_animal = None
        for enclos in self.content:
            for animal in enclos.list_animaux:
                if animal.age > age_max:
                    age_max = animal.age
                    oldest_animal = animal
        return oldest_animal

    def pass_un_jour(self)->None:
        for enclos in self.content:
            animaux_morts = []
            for animal in enclos.list_animaux:
                animal.age +=1
                animal.faim +=2
                if animal.faim > 10:
                    animaux_morts.append(animal)
                else:
                    animal.nourrir()
            for animal_mort in animaux_morts:
                enclos.list_animaux.remove(animal_mort)
            enclos.reproduction()


    def description(self)->None:
        print("\nZoo de ", self.city)

        for enclos in self.content:
            enclos.description()

# ne pas supprimer un élément du tableau qu'on est en train de parcourir
