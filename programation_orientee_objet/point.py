from math import *

class Point:
    def __init__(self, x, y, n, w, c):
        self.x = x
        self.y = y
        self.name = n
        self.weight = w
        self.color = c

    def __str__(self):
        return self.name + " : " + "(" + str(self.x) + ", " + str(self.y) + ")"

    def norme(self):
        return sqrt(self.x * self.x + self.y * self.y)
