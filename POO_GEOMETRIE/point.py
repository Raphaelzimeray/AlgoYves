from math import *
import numpy as np

class Point:
    def __init__(self, x, y, n, w, c):
        self.__x = x
        self.y = y
        self.name = n
        self.weight = w
        self.color = c

    def __str__(self):
        return self.name + " : " + "(" + str(self.__x) + ", " + str(self.y) + ")"

    def norme(self):
        return sqrt(self.__x * self.__x + self.y * self.y)

    def move(self, dx, dy):
        self.__x += dx
        self.y += dy

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.__x

    def rotate(self, angle):
        norme = self.norme()
        xn = self.__x / norme
        yn = self.y / norme
        alpha = np.arcsin(xn)
        if yn < 0:
            alpha *= -1
        self.__x = norme * cos(alpha + angle)
        self.y = norme * sin(alpha + angle)
