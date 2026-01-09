from linkedlist import *
from random import randint

list1 = Linked_list()

for i in range(10):
    list1.add_in_head(i)

list1.display()
print("")

for i in range(10):
    list1.add_in_queue(i)


list1.display()

list1.display_rec()


print("nombre d'éléments dans la liste chainée ", list1.length())

print("est ce que le chiffre 9 est présent dans ma liste ?", list1.is_inside(9))

print("est ce que le chiffre 11 est présent dans ma liste ?", list1.is_inside(11))

print("a quelle position se trouve 9 dans ma liste ?", list1.first_index_of_value(9))

print("a quelle position se trouve 7 dans ma liste ?", list1.first_index_of_value(7))

print("a quelle position se trouve 12 dans ma liste ?", list1.first_index_of_value(12))

print("supprimons 12", list1.remove_value(12))

print("a quoi ressemble la liste après la suppression de 12 ? \n")
list1.display()

print("supprimons 9", list1.remove_value(9))

print("a quoi ressemble la liste après la suppression de 9 ? \n")
list1.display()

print("supprimons 5", list1.remove_value(5))
print("a quoi ressemble la liste après la suppression de 5 ? \n")

list1.display()

print("supprimons 9 à nouveau (le dernier)", list1.remove_value(9))
print("a quoi ressemble la liste après la suppression du deuxième 9 ? \n")

list1.display()


print("insertion de 4 en position 0", list1.insert_value_by_index(4, 0))

list1.display()

print("insertion de 4 en position -4", list1.insert_value_by_index(4, -4))

print("insertion de 54 en position 3", list1.insert_value_by_index(54, 3))

list1.display()

print("on passe sur la liste 2 \n")
list2 = Linked_list()

# list2.insert_sorted_value(1)

# list2.insert_sorted_value(2)

# list2.insert_sorted_value(3)

# list2.insert_sorted_value(0)


for _ in range(20):
    list2.insert_sorted_value(randint(0, 100))

list2.display()

print("Voici la liste inversée \n")

list2.reverse()

list2.display()
