from linkedlistv2 import *
from random import randint


# list1 = Linked_list()


# print(list1.is_empty())

# list1.add_in_head(3)

# print(list1.is_empty())


# list2 = Linked_list()

# print(list2.is_empty())

# # affichage des éléments de la liste

# for i in range(10):
#     list2.add_in_head(i)

# print(list2.is_empty())

# print("Affichage list2 avec display \n")
# list2.display()

# print("Affichage list2 avec display_rec \n")
# list2.display_rec()

# list2.add_in_queue(68)

# list2.display()

# print("test de la taille de la liste 2", list2.length())

# print("test de la présence de 42 dans la liste 2", list2.is_inside(42))

# print("test de la présence de 39 dans la liste 2", list2.is_inside(39))

# print("test de la présence de 14 dans la liste 2", list2.is_inside(14))

# print("test de la présence de 5 dans la liste 2", list2.is_inside(5))

# print("test de la présence de 68 dans la liste 2", list2.is_inside(68))

# print("voyons voir à quelle position se trouve le 7", list2.first_index_of_value(7))

# print("voyons voir à quelle position se trouve le 9", list2.first_index_of_value(9))


list_3 = Linked_list()

print("voyons voir si empty marche", list_3.is_empty())

for i in range(10):
    list_3.add_in_head(i)


print("voyons voir si empty marche", list_3.is_empty())


print("voyons voir si on arrive à afficher la liste 3 avec la fonction itérative display")

list_3.display()

print("voyons voir si on arrive à afficher la liste 3 avec la fonction récursive display")

list_3.display_rec()


list_3.add_in_queue(170)

list_3.add_in_queue(231)


list_3.display()


list_3.display_rec()


print("test taille de la pile 3 (censé être 12)", list_3.length())


print("test de is inside avec 200", list_3.is_inside(200))

print("test de is inside avec 800", list_3.is_inside(800))

print("test de is inside avec 14", list_3.is_inside(14))

print("test de is inside avec 5", list_3.is_inside(5))

print("test de is inside avec 4", list_3.is_inside(4))


print("test de first value of index", list_3.first_index_of_value(7))

print("test de remove value 6", list_3.remove_value(6))

print("test de la liste 3 après avoir effacé le 6")

list_3.display()


print("test de remove value 9", list_3.remove_value(9))

list_3.display()

list_3.insert_value_by_index(150, 3)

print("\n")
list_3.display()


print("test de l'insertion en tête de liste du chiffre 400", list_3.insert_value_by_index(400, 0))

print(" voici ce que donne la liste une fois qu'on a inséré 400, \n")
list_3.display()

print(" test du comportement de la fonction avec une chiffre index négatif", list_3.insert_value_by_index(20, -4))

list_3.display()

print("test du comportement de la fonction avec un chiffre index = au max de la liste", list_3.insert_value_by_index(20, 9))

list_3.display()
