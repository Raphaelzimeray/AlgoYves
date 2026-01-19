from Animal import *
from typing import List

class Enclos:
    def __init__(self, taille_max:int):
        self.taille_max = taille_max
        self.list_animaux:List[Animal] = []
