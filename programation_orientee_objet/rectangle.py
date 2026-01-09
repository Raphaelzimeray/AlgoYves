from point import *

class Rectangle:
    def __init__(self, point_1: Point, point_2: Point, name:str):
        self.p1 = point_1
        self.p2 = point_2
        self.name = name

    def get_hauteur(self) -> float:
        return abs(self.p2.y - self.p1.y)

    def get_largeur(self) -> float:
        return abs(self.p2.x - self.p1.x)
