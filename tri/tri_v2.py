from random import randint
from time import time
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(100000)


# Exercice 1 : Permutation

tab_test = [1, 3, 8, 9, 32, 902]

def permutation(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]

print(tab_test)

permutation(tab_test, 2, 4)

print(tab_test)

# ok


# Exercice 2 : Tri classique

# Exercice 3 : Tri par Fusion

# cas de base
# si le tableau est vide il est déjà trié.
# si le tableau n'a qu'un élément, il est déjà trié
# cas récursif
# 1 diviser, séprarer le tableau en deux parties à peu près égales, de taille n/2 et n/2
# 2 régner : trier récursivement les deux parties avec l'algorithme du tri fusion
# 3 combiner : Interclasser les deux tableaux triés en un seul tableau trié

tab_test_tri_fusion = [8, 3, 5, 1]

def interclasser(tab1, tab2):
    if len(tab1) == 0:
        return tab2
    if len(tab2) == 0:
        return tab1
    if tab1[0] < tab2[0]:
        return tab1[0] + interclasser(tab1[:1], tab2)
    else:
        return tab2[0] + interclasser(tab1, tab2[:1])



def triFusion(tab):
    if len(tab) <= 1:
        return tab[0]
    half_tab = len(tab) // 2
    return interclasser(tab[:half_tab], tab[half_tab:])


print("Tri fusion test", triFusion(tab_test_tri_fusion))






# Exercice 4 : Tri Rapide

# Exercice 5 : Tri par Comptage

# Exercice 6 : Tri par insertion

# Exercice 7 : Tri par séléction

# Exercice 8 : Tri par séléction avec tests d'égalité

# Exercice 9 : Tri à bulle

# Exerice 10 : comparer tous les types de tris
