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

# ecrire une fonction qui retourne true si une valeur est dans la liste

# ecrire une fonction qui retourne l'indice d'une valeur dans la liste sachant que
# le premier maillon à pour indice 0. Si la valeur n'est pas dans la liste, ca retourne -1

# ecrire une fonction qui supprime une valeur
