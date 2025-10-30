# pile LIFO (last in first out)
# file d'attente FIFO(file queue) FIFO (first in fist out)
# Une pile en python ca va être une classe (ca peut aussi être une liste).
# On a une méthode pour créer une pile vide, savoir si la pile est vide, qu'est ce qu'il y a dans le sommet
# et on aura les deux méthodes, dépiler (retirer la dernière assiete(si il y a une assiete)), et empiler (ajouter une assiete)
# attribu taille qui donne le nombre maximum d'éléments dans la pile
# constructeur, quand on défini la méthode le premier paramètre est self obligatoirement
# un attribut c'est pour une classe "personne", l'attribut c'est nom, adresse
# getter pour retourner la valeur d'un attribut (obtenir le nom)
# setter c'est pour affecter une valeur à un attribut (changer le nom, l'age)




class Pile:
    def __init__(self, taille_max:int):
        self.__elements = []
        self.taille_max = taille_max

    def is_empty(self):
        return len(self.__elements) == 0

    def is_full(self):
        return len(self.__elements) >= self.taille_max

    def stack(self, element):
        if not self.is_full():
            self.__elements.append(element)
            return True
        return None

    def unstack(self):
        if not self.is_empty():
            return self.__elements.pop()
        return None

    def get_top(self):
        if not self.is_empty():
            return self.__elements[-1]
        return None

    # def display(self):
    #     if self.is_empty():
    #         print("Pile vide")
    #     else:
    #         print("")
    #         reversed_list = reversed(self.elements)
    #         for element in reversed_list:
    #             print(element)
    #         print("")

    def __str__(self):
        if self.is_empty():
            txt = "Pile vide"
        else:
            txt = "\n"
            reversed_list = reversed(self.__elements)
            for element in reversed_list:
                txt += str(element) + "\n"
            txt += "\n"
        return txt
