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
