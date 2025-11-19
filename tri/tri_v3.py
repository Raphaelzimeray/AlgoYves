from random import randint
from time import time
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(100000)



# Exercice 1 : Permutation

tab_test_permute = [3, 8, 10, 23]

print("tab test permute avant la permutation", tab_test_permute, "\n")

def permutation(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]


permutation(tab_test_permute, 1, 3)

print("test de la fonction permutation", tab_test_permute)



# Exercice 2 : Tri par Fusion (nlogden)


tab_test_tri_fusion = [randint(0, 100) for i in range(20)]


def interclasser(tab1, tab2):
    if len(tab1) == 0:
        return tab2
    if len(tab2) == 0:
        return tab1
    if tab1[0] <= tab2[0]:
        return [tab1[0]] + interclasser(tab1[1:], tab2)
    else:
        return [tab2[0]] + interclasser(tab1, tab2[1:])



def triFusion(tab):
    if len(tab) <= 1:
        return tab
    else:
        half_index = len(tab) // 2
        return interclasser(triFusion(tab[:half_index]), triFusion(tab[half_index:]))




# tab_test = [2, 3, 4, 5]

# print(tab_test[:2])

print("test de tab test tri fusion avant la fonction", tab_test_tri_fusion)

trifusionresult = triFusion(tab_test_tri_fusion)

print("test de tab test tri fusion après la fonction", trifusionresult)



# Exercice 3 : Tri Rapide (nlogden)


# Exercice 4 : Tri par Comptage (O(n))


# Exercice 5 : Tri par insertion (quadratique)


tab_test_tri_insertion = [23, 6, 3, 4]


def triIntersion(tab):
    for i in range(len(tab) - 1):
        print("Nous rentrons dans la boucle numéro ", i)
        var_temp = tab[i+1]
        print("var temp", var_temp)
        print("i avant le while", i)
        j = i
        while j >= 0 and var_temp >= tab[j]:
            print("j dans mon while", j)
            print("tab[j+1] dans mon while", tab[j+1])
            print("tab[j] dans mon while", tab[j], "\n")
            tab[j+1] = tab[j]
            j = j-1
        tab[j] = var_temp
        print("test de tab[i] après les boucles while (on est dans la boucle for) : ", tab[i], " ici i vaut : ", i)
        print("voici l'état du tableau à la fin du tour de boucle numéro : ", i, tab, "\n")


print(tab_test_tri_insertion)

triIntersion(tab_test_tri_insertion)

print("tab test tri insertion après être passé par la fonction", tab_test_tri_insertion)


# Version corrigée de Yves


def tri_par_insertion(tableau):
    for i in range(1,len(tableau)):
        x = tableau[i]
        j = i
        while j>0 and tableau[j-1]>=x:
            tableau[j] = tableau[j-1]
            j-=1
        tableau[j] = x
    return tableau


# Version premier cours

def insert_sort(tab):
    for i in range(1, len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j -1]
            j = j - 1
        tab[j] = x



# Explication

# test de mon code avec un tableau à 4 éléments [23, 6, 3, 4]

# TOUR DE BOUCLE 2 (i vaut 1)





# 2 e essai tri insertion


tab_test_3_insertion = [randint(0, 100) for i in range(20)]


def tri_insertion_3(tab):
    for i in range(1, len(tab)):
        var_temp = tab[i]
        j = i
        while j >=0 and tab[j-1] > var_temp:
            tab[j] = tab[j-1]
            j -=1
        tab[j] = var_temp



print("tableau avant le 3 e essai de l'insertion", tab_test_3_insertion)

tri_insertion_3(tab_test_3_insertion)

print("tableau après le 3 e essai de l'insertion", tab_test_3_insertion)






# Exercice 6 : Tri par séléction (quadratique)


tab_test_select_sort = [randint(0, 100) for i in range(20)]

def select_sort(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        permutation(tab, min_index, i)


print("test de mon tri par selection avant le tri", tab_test_select_sort)

select_sort(tab_test_select_sort)

print("test de mon tableau select sort après le tri", tab_test_select_sort)



# Exercice 7 : Tri par séléction avec tests d'égalité (quadratique)


# Exercice 8 : Tri à bulle (quadratique)


tab_bubble_sort = [4, 2, 3, 1]

def bubble_sort(tab):
    for i in range(len(tab) -1):
        for j in range(len(tab) - 1 - i):
            if tab[j] > tab[j+ 1]:
                permutation(tab, j, j+1)


print("test des tableaux à bulle", tab_bubble_sort)

bubble_sort(tab_bubble_sort)

print("test du tableau à bulle post fonction", tab_bubble_sort)



# Exercice 9 : Comparaison des tris


tab_bubble_sort = [4, 2, 3, 1]

def sort_test(tab):
    for i in range(len(tab) -1):
        for j in range(len(tab)-1 - i):
            if tab[j + 1] < tab[i]:
               permutation(tab, j+1, j)

sort_test(tab_bubble_sort)

print(tab_bubble_sort)
