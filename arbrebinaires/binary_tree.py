# data, right, left

class Node:
    def __init__(self, value:int, right:'Node'=None, left:'Node'=None):
        self.value = value
        self.right = right
        self.left = left

    def size(self) -> int:
        if not self.right and not self.left:
            return 1
        else:
            right_size = 0
            left_size = 0
            if self.right:
                right_size = self.right.size()
            if self.left:
                left_size = self.left.size()
            return 1 + right_size + left_size

    # avoir la profondeur (height)

    def profondeur(self) -> int:
        if not self.right and not self.left:
            return 1
        else:
            right_prof = 0
            left_prof = 0
            if self.right:
                right_prof = self.right.profondeur()
            if self.left:
               left_prof = self.left.profondeur()
        return 1 + max(right_prof, left_prof)


    # avoir le nombre de feuilles (les extrémités)

    def number_of_feuilles(self) -> int:
        if not self.right and not self.left:
            return 1
        else:
            right_tree = 0
            left_tree = 0
            if self.right:
                right_tree = self.right.number_of_feuilles()
            if self.left:
                left_tree = self.left.number_of_feuilles()
            return right_tree + left_tree

    # prefixe => commencer par la racine (5), puis sous arbre gauche puis sous arbre droit
    # infixe => on commmence par le sous arbre gauche, puis la racine, puis sous arbre droit
    # suffixe / postfix => sous arbre gauche, sous arbre droit, racine
    # parcours en largeur => consiste à afficher par niveaux (5, (3-7), (2-4-6-8), 1)

    def display_infixe(self):
        if self.left:
            self.left.display_infixe()
        print(self.value, end=" ")
        if self.right:
            self.right.display_infixe()

    def display_prefixe(self):
        print(self.value, end=" ")
        if self.left:
            self.left.display_prefixe()
        if self.right:
            self.right.display_prefixe()

    def display_suffixe(self):
        if self.left:
            self.left.display_suffixe()
        if self.right:
            self.right.display_suffixe()
        print(self.value, end=" ")

    # exercice : chercher si une valeur est dans un arbre binaire de recherche (pour tout noeud, la valeur du sous arbre gauche est < strictement inférieur et le sous arbre droit > strictement supérieur)
    # inserer une valeur au bon endroit dans un arbre binaire de recherche
    # affichage en largeur

    def is_in_tree(self, num) -> bool:
        if self.value == num:
            return True
        if self.left and num < self.value:
            return self.left.is_in_tree(num)
        if self.right and num > self.value:
            return self.right.is_in_tree(num)
        return False

    def insert_element(self, num):
        if num < self.value:
            if not self.left:
                self.left = Node(num)
            else:
                self.left.insert_element(num)
        elif num > self.value:
            if not self.right:
                self.right = Node(num)
            else:
                self.right.insert_element(num)


    def get_list_infixe(self):
        list_infixe = []
        def _get_list_infixe(node:Node):
            if node.left:
                _get_list_infixe(node.left)
            list_infixe.append(node.value)
            if node.right:
                _get_list_infixe(node.right)

        _get_list_infixe(self)
        return list_infixe


