# from binarytree import Node
from binary_tree import *
from random import randint, seed


def sorted_list(unsorted_list:list):
    root = Node(unsorted_list[0])
    unsorted_list.pop(0)
    while unsorted_list:
        root.insert_element(unsorted_list.pop())
    root.display_infixe()
    for e in root.get_list_infixe():
        unsorted_list.append(e)




# Création d'un ABR
# root = Node(5)
# root.left = Node(3)
# root.right = Node(7)
# root.left.left = Node(2)
# root.left.right = Node(4)
# root.right.left = Node(6)
# root.right.right = Node(8)
# root.left.left.left = Node(1)

# # Affichage élégant
# print(root)
# seed(42)

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.right = Node(4)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.right.left = Node(6)
root.right.right = Node(8)



print("Taille de l'arbre (nombre de noeud au total) : ", root.size())
print("Profondeur de l'arbre: ", root.profondeur())
print("Nombre de feuilles de l'arbre: ", root.number_of_feuilles())
print("Affichage infixe: ")
root.display_infixe()
print("Test de la présence de 0 dans l'arbre :", root.is_in_tree(0))
print("Test de la présence de 4 dans l'arbre :", root.is_in_tree(4))
print("Test de la présence de 10 dans l'arbre :", root.is_in_tree(10))


root2 = Node(10)
for _ in range(15):
    root2.insert_element(randint(0, 20))

root2.display_infixe()

# root2.get_list_infixe()

list_test = root2.get_list_infixe()

print("print root2 de get list infixe: ", list_test)

list_unsorted = [randint(0, 20) for _ in range(20)]

print("test de list unsorted", list_unsorted)

sorted_list(list_unsorted)

print("test de list unsorted après tri par l'ABR", list_unsorted)
