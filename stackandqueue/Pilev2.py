class Pile:
    # pourquoi le éléments n'est pas dans les paramètres
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
    # ok

    def unstack(self):
        if not self.is_empty():
            return self.__elements.pop()
        return None

    #ok


    def get_top(self):
        if not self.is_empty():
            return self.__elements[-1]
        return None

    # ok

    # taille de la pile

    def number_of_elements(self):
        return len(self.__elements)


    def reverse_stack(self) -> None:
        pile2 = Pile(self.taille_max)
        pile3 = Pile(self.taille_max)
        while not self.is_empty():
            pile2.stack(self.get_top())
            self.unstack()
        while not pile2.is_empty():
            pile3.stack(pile2.get_top())
            pile2.unstack()
        while not pile3.is_empty():
            self.stack(pile3.get_top())
            pile3.unstack()

    #ok

    # max de la pile

    def max(self):
        if self.is_empty():
            return None
        max_val = self.get_top()
        pile2 = Pile(self.taille_max)
        while not self.is_empty():
            if self.get_top() >= max_val:
                max_val = self.get_top()
            pile2.stack(self.unstack())
        while not pile2.is_empty():
            self.stack(pile2.unstack())
        return max_val

    # max d'une partie de la pile

    def partial_max(self, profondeur):
        if self.is_empty():
            return None
        max_val = self.get_top()
        pile2 = Pile(profondeur)
        count = 0
        while not self.is_empty() and count < profondeur:
            if self.get_top() > max_val:
                max_val = self.get_top()
            pile2.stack(self.unstack())
            count +=1
        while not pile2.is_empty():
            self.stack(pile2.unstack())
        return max_val


    # index du max d'une partie de la pile

    def partial_max_index(self, profondeur):
        if self.is_empty():
            return None
        max_val = self.get_top()
        pile2 = Pile(profondeur)
        count = 0
        index = 0
        while not self.is_empty() and count < profondeur:
            if self.get_top() > max_val:
                max_val = self.get_top()
                index = count
            pile2.stack(self.unstack())
            count += 1
        while not pile2.is_empty():
            self.stack(pile2.unstack())
        return index

        #ok






    # inversion d'une partie de la pile



    def partial_reverse(self, profondeur):
        if self.is_empty():
            return None
        pile2 = Pile(profondeur)
        pile3 = Pile(profondeur)
        count = 0
        while not self.is_empty() and count < profondeur:
            pile2.stack(self.unstack())
            count +=1
        while not pile2.is_empty():
            pile3.stack(pile2.unstack())
        while not pile3.is_empty():
            self.stack(pile3.unstack())

    # ok




    # affichage des éléments

    def __str__(self):
        if self.is_empty():
            txt ="La liste est vide"
        else:
            txt = "\n"
            reversed_list = reversed(self.__elements)
            for element in reversed_list:
                txt += str(element) + "\n"
            txt += " \n"
        return txt




    # tri d'une pile

    def order_elements(self):
        if self.is_empty():
            return None
        for profondeur in range(len(self.__elements), 0, -1):
            #print("test de profondeur dans la boucle de for profondeur \n", profondeur)
            #print("test de partial max index à chaque tour de boucle for prondeur", self.partial_max_index(profondeur))
            self.partial_reverse(1 + self.partial_max_index(profondeur))
            #print("à la profondeur ", profondeur, " après le 1er partial reverse voici l'état de la pile ", self)
            self.partial_reverse(profondeur)
            #print("à la profondeur ", profondeur, " après le 2nd partial reverse voici l'état de la pile ", self)
