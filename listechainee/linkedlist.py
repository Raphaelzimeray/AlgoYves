class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def is_empty(self)-> bool:
        return self.head == None

    def add_in_head(self, value):
        node = Node(value, self.head)
        self.head = node

    def display(self):
        if self.is_empty():
            print("la liste est vide")
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next

    def display_rec(self):
        def display_node(node:Node):
            if node is None:
                print("la liste est vide")
            else:
                print(node.value)
                display_node(node.next)

        display_node(self.head)


    def add_in_queue(self, value):
        node = Node(value)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = node



# ecrire une fonction qui retourne la longueur de la liste

    def length(self)-> int:
        if self.is_empty():
            return 0
        current_node = self.head
        count_elements = 0
        while current_node !=None:
            current_node = current_node.next
            count_elements +=1
        return count_elements

# ecrire une fonction qui retourne true si une valeur est dans la liste

    def is_inside(self, value) -> bool:
        if self.is_empty():
            return False
        current_node = self.head
        while current_node!= None and current_node.value != value:
            current_node = current_node.next
        if current_node == None:
            return False
        return True




# ecrire une fonction qui retourne le premier indice d'une valeur dans la liste sachant que
# le premier maillon à pour indice 0. Si la valeur n'est pas dans la liste, ca retourne -1

    def first_index_of_value(self, value) -> int:
        if self.is_empty():
            return -1
        index_of_value = 0
        current_node = self.head
        while current_node != None and current_node.value != value:
            current_node = current_node.next
            index_of_value +=1
        if current_node == None:
            return -1
        return index_of_value

# ecrire une fonction qui supprime une valeur

    def remove_value(self, value) -> bool:
        if self.is_empty():
            return False
        current_node = self.head
        if current_node.value == value:
            self.head = current_node.next
            del current_node
            return True

        prec_node = self.head
        current_node = current_node.next
        while current_node !=None and current_node.value !=value:
            current_node = current_node.next
            prec_node = prec_node.next
        if current_node == None:
            return False
        prec_node.next = current_node.next
        del current_node
        return True

# ecrire une fonction qui insert un élément à un indice (si indice supérieur à la longeur de la liste je le mets à la fin,
# et si l'indice = 0 c'est que je mets le maillon en tête de chaine).
# et si c'est négatif on retourne false
# on retournera un booléen

    def insert_value_by_index(self, value, index) -> bool:
        if index < 0:
            return False
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
            return True
        current_node = self.head
        count = 0
        while current_node !=None and count < index -1:
            current_node = current_node.next
            count +=1
        node.next = current_node.next
        current_node.next = node
        return True




    # inserer en ordre croissant (juste après le premier élément plus petit que)

    def insert_sorted_value(self, value) -> None:
        if self.is_empty() or self.head.value > value:
            self.add_in_head(value)
            return None
        current_node = self.head
        while current_node.next != None and current_node.next.value < value:
            current_node = current_node.next
        if current_node.next == None:
            self.add_in_queue(value)
            return None
        node = Node(value)
        node.next = current_node.next
        current_node.next = node
        return None

    # je fourni une liste non triée(tableau classique pas liste chainée), et ca retourne une liste triée.

    def reverse(self):
        if self.is_empty():
            print("la liste est vide")
        current_node = self.head
        prec_node = None
        while current_node !=None:
            current_node_next = current_node.next
            current_node.next = prec_node
            prec_node = current_node
            current_node = current_node_next
        self.head = prec_node
