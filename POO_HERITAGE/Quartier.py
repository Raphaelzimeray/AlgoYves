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
