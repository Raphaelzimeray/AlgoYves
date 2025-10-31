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

# RECURSION 1.1.1 - EXECUTION 2.1.1 => Trifusion([76]). on rentre dans la condition d'arret
# on retoune le tableau T [76].

# RÉCURSION 1.1.2 - EXECUTION 2.1.2 => Trifusion([2]). on rentre dans la condition d'arret
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


# Tri par fusion

def interclasser(tab1, tab2):
    if len(tab1) == 0:
        return tab2
    if len(tab2) == 0:
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
        indice = len(tab) // 2
        return interclasser(triFusion(tab[:indice]),
                            triFusion(tab[indice:]))



# Tri rapide


def partitionner(tab, first, last, pivot):
    permute(tab, pivot, last)
    j = first
    for i in range(first, last):
        if tab[i] <= tab[last]:
            permute(tab, i, j)
            j = j + 1
    permute(tab, last, j)
    return j

def quick_sort(tab, first_index, last_index):
    if first_index < last_index:
        pivot = randint(first_index, last_index)
        pivot = partitionner(tab, first_index, last_index, pivot)
        quick_sort(tab, first_index, pivot -1)
        quick_sort(tab, pivot + 1, last_index)



# Décomposition du tri Rapide avec un tab_to_sort = [3, 7, 8, 5, 9] (5 éléments)

# EXECUTION 1 de Quick sort. quick_sort(tab, first_index, last_index)
# quick_sort(tab_to_sort, 0, len(tab_to_sort)-1)
# je test si first_index < last_index: => 0 < len(tab) -1 => 0 < 5 -1 => 0 < 4, ca renvoie true, on rentre dans le if
# pivot = randint(first_index, last_index) => randit(0, 4) (équivalent de dire, je te laisser choisir une valeur entière aléatoire entre 0 et 4)
# pivot = partitionner(tab, first_index, last_index, pivot). donc pivot recoit ce que retourne la fonction partitionner(tab_to_sort, firstindex, last_index, pivot)
# on va décider que randint à renvoyé 3 pour pivot
# partitionner(tab_to_sort, 0, 4, 3)
# Je ne peux pas continuer à execucter la fonction quick_sort, n'ayant pas de réponse sur la valeur de pivot (elle est en attente)

# EXECUTION 1 de partitionner. partitionner(tab, first, last, pivot) => partitionner(tab_to_sort, 0, 4, 3)
# je rentre et j'appelle tout de suite la fonction permute en lui passant 3 paramètres (tab, pivot, last) => (tab_to_sort, 3, 4)
# la fonction permute va placer le pivot en dernière position du tableau. tab[pivot], tab[last] = tab[last], tab[pivot]
# ce qui donne => tab[3], tab[4] = tab[4], tab[3] => 5 et 9 sont permutés
# mon tableau tab_to_sort à ce stade vaut donc [3, 7, 8, 9, 5], j'ai mis l'élément à l'indice du pivot en dernier
# j = first => j = 0
# je fais une boucle for avec un indice i qui va du premier(first=0) à l'avant dernier (last=4) donc ca s'arrete à last -1 (3).
# TOUR BOUCLE 1 -> je test si tab[i] <= tab[last]
# => tab[0] <= tab[4] (la valeur de mon pivot, 5, pour les cas de l'EXECUTION 1 de partitionner, tab[last] sera égal à 5)
# => 3 <= 5, ca renvoie true, je rentre dans le if
# je rappelle permute(tab, i, j) => permute(tab_to_sort, 0, 0)
# donc je permute rien, je permute le même élément.
# j'incrémente j = j + 1 => 0 + 1 => 1 j = 1
# TOUR BOUCLE 2 -> je test si tab[i] <= tab[last]
# => tab[1] <= tab[4] => 7 <= 5, cette condition renvoie false, je ne rentre pas dans mon if, et je passe au tour de boucle suivant
# TOUR BOUCLE 3 -> je test si tab[i] <= tab[last]
# => tab[2] <= tab[4] => 8 <= 5, cette condition renvoie false, je ne rentre pas dans mon if, et je passe au tour de boucle suivant
# TOUR BOUCLE 4 -> je test si tab[i] <= tab[last]
# => tab[3] <= tab[4] => 9 <=5, cette condition renvoie false, je ne rentre pas dans mon if, et je passe au tour de boucle suivant
# il n'y a pas de tour 5, parce que l'indice 3 du tableau c'est l'indice maximal de i
# FIN DE LA BOUCLE
# je fais la permutation permute(tab, last, j) en tenant compte du fait que j est égal à 1.
# permute(tab_to_sort, 4, 1)
# tableau après la fin de la première execution de partitionner tab_to_sort = [3, 5, 8, 9, 7]
# avec une valeur de retour qui est égale à j donc 1.

# RETOUR EXECUTION 1 de quick_sort.
# Je suis maintenant fixé sur la valeur de pivot, qui est égale à 1 pivot = 1, je peux passer aux lignes de code suivantes
# deux appels de la fonction quick_sort(tab, first_index, pivot -1) => quick_sort(tab_to_sort, 0, 0)
# je ne vais pas faire le 2 e appel récursif de  quick_sort(tab, pivot + 1, last_index) tant que la réponse de la fonction
# précédente ne m'est pas parvenue

# RÉCURSION 1.1 - EXECUTION 2 de quick_sort.
# quick_sort(tab, first_index, pivot -1)
# quick_sort(tab_to_sort, 0, 0)
# if first_index < last_index:
# if 0 < 0, cette condition renvoie false, pas d'execution de la suite
# on a voulu trier ce qui est à gauche du pivot dans le tableau, c'est à dire le tableau [3], donc on ne rentre pas dans ce if

# code quick sort pour aider à l'écriture
# def quick_sort(tab, first_index, last_index):
#     if first_index < last_index:
#         pivot = randint(first_index, last_index)
#         pivot = partitionner(tab, first_index, last_index, pivot)
#         quick_sort(tab, first_index, pivot -1)
#         quick_sort(tab, pivot + 1, last_index)

# RÉCURSION 1.2 - EXECUTION 3 de quick_sort
# quick_sort(tab, pivot + 1, last_index)
# ici, on va vouloir opérer sur les éléments qui se situent à droite du pivot
# quick_sort(tab_to_sort, 2, 4)
# if first_index < last_index:
# if 2 < 4, ca renvoie true, on poursuit
# pivot = un chiffre aléatoire entre 2 et 4 (on va dire que c'est 2)
# ligne suivante, pivot recoit l'appel de partitionner(tab, first_index, last_index, pivot)
# partitionner(tab_to_sort, 2, 4, 2)

# def partitionner(tab, first, last, pivot):
#     permute(tab, pivot, last)
#     j = first
#     for i in range(first, last):
#         if tab[i] <= tab[last]:
#             permute(tab, i, j)
#             j = j + 1
#     permute(tab, last, j)
#     return j

# EXECUTION 2 de partitionner((tab_to_sort, 2, 4, 2)
# j'appelle la fonction permute(tab, pivot, last), et je place le pivot en bout de tableau
# permute(tab2sort, 2, 4) donc le tableau [3, 5, 8, 9, 7] va devenir => [3, 5, 7, 9, 8]
# j = first, donc 2. j = 2, je n'utilise plus la partie gauche du tableau, j'utilise [7,9,8]
# je fais une boucle for qui va de l'indice 2, à l'indice 4. Quand j'ai un range de 2 paramètres, range(a,b),
# le i va de a à b-1.
# Ici j'ai range de (2,4) donc je vais faire premier tour i =2, deuxième tour i=3, et je m'arrête la car j'ai parcouru de 2 à 3.
# i va valoir 2, puis i va valoir 3
# PREMIER TOUR DE BOUCLE FOR avec i=2
# if tab[i] <= tab[last]:
# if tab[2] <= tab[4]
# if 7 <=8, c'est bien le cas, cette condition renvoie true
# je rentre dans le if
# j'appel permute et je bascule l'élément i avec l'élément j. (i=2 et j=2) je ne fais rien
# j'incrémente j = j + 1 => j = 3
# DEUXIÈME TOUR DE BOUCLE FOR avec i =3
# if tab[3] <=tab[4]
# if 9<=8, ca renvoie false, on ne rentre pas dans le if, et les boucles sont terminées
# je rappel permute(tab, last, j) pour ramener le pivot à la frontière entre les deux parties du tableau (les parties <= à lui, et les parties > à lui)
# le tableau maintenant est diposé comme ceci : [3, 5, 7, 8, 9]
# la chose qui a changée c'est la qu'on a modifié la position du pivot
# return j, donc return 3

# RETOUR RÉCURSION 1.2 - EXECUTION 3 de quick_sort
# maintenant on est fixé sur pivot, qui vaut 3, on peut poursuivre notre execution
# j'appelle quick_sort(tab, first_index, pivot -1)
# quick_sort(tab2sort, 2, 2)

# RECUSION 2.1 - EXECUTION 4 de quick_sort((tab2sort, 2, 2)
# je ne vais pas rentrer dans le if first_index < last_index
# 2 < 2 renvoie false !

# RÉCURSION 2.2 - EXECUTION 5  de quick_sort(tab, pivot + 1, last_index)
# quick_sort(tab2sort, 4, 4)
# meme chose que pour récursion 2.1 excution 4 de quick sort, je ne vais  pas rentrer dans le if first_index < last_index
# 4 < 4 renvoie false !

# le code est terminé, il n'y a plus d'appel à partitionner, ou d'autres appels récursifs de quick_sort, le tableau est trié



# Tri


min = 1000
max = 20000
step = 1000

X = [x for x in range(min, max, step)]

Y = []


# print(" debut tri basique")
# for i in range (min, max, step):
#     print(i, end=" ", flush=True)
#     tab_unsorted = [randint(0,i//2) for _ in range(i)]
#     start = time()
#     f = sort_tab(tab_unsorted)
#     stop = time()
#     Y.append(stop - start)

# plt.plot(X,Y,label='tri basique')

# Y = []

# print("debut tri à bulle v2")

# for i in range (min, max, step):
#     print(i, end=" ", flush=True)
#     tab_unsorted = [randint(0,i//2) for _ in range(i)]
#     start = time()
#     f = bubble_sort2(tab_unsorted)
#     stop = time()
#     Y.append(stop - start)

# plt.plot(X,Y,label='tri à bulle v2')


print("debut tri fusion")

for i in range (min, max, step):
    print(i, ":", end=" ", flush=True)
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    start = time()
    f = triFusion(tab_unsorted)
    stop = time()
    Y.append(stop - start)
    for i in range(5):
        print(f[i], end=" ")
    print("...", end=" ")
    for i in range(len(f) -5, len(f)):
        print(f[i], end=" ")
    print(" ")
plt.plot(X,Y,label='tri Fusion')


Y = []

print("debut tri rapide")

for i in range (min, max, step):
    print(i, ":", end=" ", flush=True)
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    start = time()
    f = quick_sort(tab_unsorted, 0, len(tab_unsorted)-1)
    stop = time()
    Y.append(stop - start)
    for i in range(5):
        print(tab_unsorted[i], end=" ")
    for i in range(len(tab_unsorted) -5, len(tab_unsorted)):
        print(tab_unsorted[i], end=" ")
    print(" ")


plt.plot(X,Y,label='tri rapide')
plt.legend()
plt.show()
