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

    # taille de la pile

    def number_of_elements(self):
        return len(self.__elements)


    def reverse_stack(self) -> None:
        pile2 = Pile(self.taille_max)
        pile3 = Pile(self.taille_max)
        while not self.is_empty():
            pile2.stack(self.unstack())
        while not pile2.is_empty():
            pile3.stack(pile2.unstack())
        while not pile3.is_empty():
            self.stack(pile3.unstack())


    # max de la pile

    def max(self):
        if self.is_empty():
            return None
        max = self.get_top()
        pile2 = Pile(self.taille_max)
        while not self.is_empty():
            if self.get_top() > max:
                max = self.get_top()
            pile2.stack(self.unstack())
        while not pile2.is_empty():
            self.stack(pile2.unstack())
        return max



    # max d'une partie de la pile

    def partial_max(self, profondeur):
        if self.is_empty():
            return None
        max = self.get_top()
        pile2 = Pile(self.taille_max)
        count = 0
        while not self.is_empty() and count < profondeur:
            if self.get_top() > max:
                max = self.get_top()
            pile2.stack(self.unstack())
            count +=1
        while not pile2.is_empty():
            self.stack(pile2.unstack())
        return max

    # index du max d'une partie de la pile

    def partial_max_index(self, profondeur):
        if self.is_empty():
            return None
        max = self.get_top()
        max_index = 1
        pile2 = Pile(self.taille_max)
        count = 1
        while not self.is_empty() and count <= profondeur:
            if self.get_top() > max:
                max = self.get_top()
                max_index = count
            pile2.stack(self.unstack())
            count +=1
        while not pile2.is_empty():
            self.stack(pile2.unstack())
        return max_index


    # inversion d'une partie de la pile
    def partial_reverse(self, profondeur):
        pile2 = Pile(self.taille_max)
        pile3 = Pile(self.taille_max)
        count = 0
        while not self.is_empty() and count < profondeur:
            pile2.stack(self.unstack())
            count +=1
        while not pile2.is_empty():
            pile3.stack(pile2.unstack())
        while not pile3.is_empty():
            self.stack(pile3.unstack())



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

    def order_elements(self):
        i = self.number_of_elements()
        while i > 0:
            j = self.partial_max_index(i)
            self.partial_reverse(j)
            self.partial_reverse(i)
            i -=1
