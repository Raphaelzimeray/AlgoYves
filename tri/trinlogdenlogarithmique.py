# Décomposition sur tableau à 4 éléments

# Testtab = [76, 2, 21, 9]

# Deux fonctions : tri fusion et interclasser
# https://fr.wikipedia.org/wiki/Tri_fusion#Algorithme

# Trifusion ca prend un tableau en paramètres
# Interclasser il prend deux tableaux triés, et retourne un tableau trié contenant l'ensemble
# des éléments

# EXECUTION 1 de Trifusion => Trifusion([76, 2, 21, 9]). on ne rentre pas
# dans la condition d'arret n <= 1. On passe dans le else
# on retourne l'appel de la fonction interclasser en lui passant 2 paramètres
# l'appel des fonctions triFusion avec les deux moitiés de tableau
# on retourne interclasser(Trifusion([76,2]), Trifusion([21,9]))
# on est dans le même cas que fibonnaci avec une ampleur beaucoup
# moins importante, c'est logarithmique au lieu d'être exponentiel
# je ne peux pas executer pour le moment interclasser parce que il me
# faut d'abord la valeur des paramètres

# RECURSION 1.1 - EXECUTION 1.1 => Trifusion([76,2]). on ne rentre pas dans la condition
# d'arrêt, on passe dans le else.
# on retourne l'appel de la fonction interclasser en lui passant 2 paramètres
# l'appel des fonctions triFusion avec les deux moitiés de tableau
# on retourne interclasser(Trifusion([76]), Trifusion([2]))

# RECURSION 2.1 - EXECUTION 2.1 => Trifusion([76]). on rentre dans la condtion d'arret
# on retoune le tableau T [76].

# RÉCURSION 2.2 - EXECUTION 2.2 => Trifusion([2]). on rentre dans la condition d'arret
# on retourne le tableau T [2]

# ON COMMENCE À REMONTER - RETOUR RECURSION 1.1 - EXECUTION 1.1
# j'ai maintenant la réponse, je suis fixé sur la valeur de trifusion([76]),
# et Trifusion([2]) donc j'execute interclasser([76], [2]).

# EXECUTION 1 de Interclasser([76], [2]).
# aucun des deux tableaux n'est vide
# on arrive à A[0] <= B[0] donc
# 76 <=2, cette condition renvoie false, on passe donc dans le else
# on rentre dans le sinon
# je renvoie B[0] + interclasser(A, B[dont on a retiré le premier élément])
# je renvoie B[0] + interclasser(A, B[1:])
# je renvoie [2] +  interclasser([76], [])

# RECURSION 1 - EXECUTION 2 de Interclasser([76], [])
# B est vide, donc on renvoie A
# A = [76]

# RETOUR EXECUTION 1 DE Interclasser([76, [2]])
# je renvoie [2] +[76] => [2, 76]

from random import randint
from time import time
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(100000)

# Permutation
def permute(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]

# Tri classique

def sort_tab(tab):
    tab_sorted = tab[:]
    for j in range(len(tab_sorted) - 1):
        min_value_index = j
        for i in range(j, len(tab_sorted)):
            if tab_sorted[i] < tab_sorted[min_value_index]:
                min_value_index = i
        permute(tab_sorted, j, min_value_index)
    return tab_sorted

# Tri à bulle v2

def bubble_sort2(tab):
    for i in range(len(tab)):
        indice_val_max = i
        for j in range(len(tab)-1 - i):
            if tab[j] > tab[indice_val_max]:
                indice_val_max = j
        permute(tab, len(tab) -1 -i, indice_val_max)



def interclasser(tab1, tab2):
    if not tab1:
        return tab2
    if not tab2:
        return tab1
    if tab1[0] <= tab2[0]:
        return [tab1[0]] + interclasser(tab1[1:], tab2)
    else:
        return [tab2[0]] + interclasser(tab1, tab2[1:])


# Tri par fusion
def triFusion(tab):
    if len(tab) <= 1:
        return tab
    else:
        return interclasser(triFusion(tab[:len(tab) //2]),
                            triFusion(tab[len(tab) //2:]))




min = 10
max = 100
step = 10

X = [x for x in range(min, max, step)]

Y = []


print(" debut tri basique")
for i in range (min, max, step):
    print(i, end=" ", flush=True)
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    tab_unsorted.sort()
    permute(tab_unsorted, 5, len(tab_unsorted) - 5)
    start = time()
    f = sort_tab(tab_unsorted)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='tri basique')

Y = []

print("debut tri fusion")

for i in range (min, max, step):
    print(i, end=" ", flush=True)
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    tab_unsorted.sort()
    permute(tab_unsorted, 5, len(tab_unsorted) - 5)
    start = time()
    f = triFusion(tab_unsorted)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='tri Fusion')

Y = []

print("debut tri à bullle v2")

for i in range (min, max, step):
    print(i, end=" ", flush=True)
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    tab_unsorted.sort()
    permute(tab_unsorted, 5, len(tab_unsorted) - 5)
    start = time()
    f = bubble_sort2(tab_unsorted)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='tri à bulle v2')


plt.legend()
plt.show()
