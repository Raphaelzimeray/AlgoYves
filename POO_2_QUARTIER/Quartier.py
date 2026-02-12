from Batiment import *
from typing import List


class Quartier:
    def __init__(self):
        self.list_batiments:List[Batiment] = []


    def add_batiment(self, b:Batiment):
        self.list_batiments.append(b)

    def display_category(self, cat:int):
        for batiment in self.list_batiments:
            if batiment.get_category() >= cat:
                print(batiment)

    # Plus grand batiment du quartier

    def plus_grand_batiment(self) -> Batiment:
        biggest_batiment = None
        for batiment in self.list_batiments:
            if biggest_batiment == None:
                biggest_batiment = batiment
            else:
                if batiment.surface > biggest_batiment.surface:
                    biggest_batiment = batiment
        return biggest_batiment


    # Version pythonnesque

    def plus_grand_batiment_2(self) -> Batiment:
        return sorted(self.list_batiments, key= lambda bat: bat.surface, reverse=True)[0]

    # Version pythonnesque sans lambda avec fonction de base normale



    def plus_grand_batiment_3(self) -> Batiment:
        def get_surface(batiment:Batiment):
            return batiment.surface
        return sorted(self.list_batiments, key= get_surface, reverse=True)[0]
