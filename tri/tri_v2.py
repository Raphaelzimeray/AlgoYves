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


# Exercice 2 : Tri classique (quadratique)

# Exercice 3 : Tri par Fusion (nlogden)

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
        return [tab1[0]] + interclasser(tab1[1:], tab2)
    else:
        return [tab2[0]] + interclasser(tab1, tab2[1:])



def triFusion(tab):
    if len(tab) <= 1:
        return tab
    half_tab = len(tab) // 2
    return interclasser(triFusion(tab[:half_tab]), triFusion(tab[half_tab:]))


print("Tri fusion test", triFusion(tab_test_tri_fusion))


# print("test de tab test tri fusion [:2]", tab_test_tri_fusion[:2])
# print("test de tab test tri fusion [2:]", tab_test_tri_fusion[2:])


# Décomposition avec le tableau tab_test_tri_fusion = [8, 3, 5, 1]

# EXECUTION 1 - triFusion([8, 3, 5, 1])
# if len(tab) <= 1: => if 4 <=1, cette condition renvoie false
# half_tab = len(tab) //2 => 4//2 => 2
# on passe au return interclasser(triFusion(tab[:half_tab]), triFusion(tab[half_tab:]))
# return interclasser(triFusion(tab[:2]), triFusion(tab[2:]))
# return interclasser(triFusion([8, 3]), triFusion([5, 1]))
# Je suis dans l'impossibilité d'executer interclasser parce que ne connais pas les valeurs des paramètres que je lui ai passé
# donc la prochaine étape, ca va être de savoir ce que valent ces deux paramètres que j'ai passés à la fonction interclasser



# RECURSION 1.1 - EXECUTION 2.1 - triFusion([8, 3])
# if len(tab) <= 1: => if 2 <= 1, cette condition renvoie false
# half_tab = len(tab) //2 => 2//2 => 1
# on passe au return interclasser(triFusion(tab[:half_tab]), triFusion(tab[half_tab:]))
# return interclasser(triFusion(tab[:1]), triFusion(tab[1:]))
# return interclasser(triFusion([8]), triFusion([3]))

# RECURSION 1.1.1 - EXECUTION 2.1.1 - triFusion([8])
# if len(tab) <= 1: => if 1 <= 1, cette condition renvoie true, on rentre dans le if
# on retourne tab => on retourne [8]

# RECURSION 1.1.2 - EXECUTION 2.1.2 - triFusion([3])
# if len(tab) <= 1: => if 1 <= 1, cette condition renvoie true, on rentre dans le if
# on retourne tab => on retourne [3]

# RETOUR RECURSION 1.1 - EXECUTION 2.1 - triFusion([8,3])
# je suis maintenant fixé sur la valeur de triFusion([8]), et triFusion([3])
# je vais pouvoir executer la fonction interclasser([8], [3])
# donc la, l'execution de interclasser([8], [3]) va me permettre de pouvoir aussi savoir ce que vaut triFusion([8,3]) puisque c'est
# précisément ce que retourne la fonction interclasser([8], [3])

# EXECUTION 1 de interclasser([8], [3])
# je ne tombe pas dans les 2 premiers ifs if len(tab1) == 0: et  if len(tab2) == 0:
# if tab1[0] < tab2[0]:
# if 8 < 3
# cette condition renvoie false, je passe dans le else
# return [tab2[0]] + interclasser(tab1, tab2[1:])
# return [3] + interclasser([8], [])
# je ne connais pas la valeur de interclasser, je suis obligé de la calculer

# RECURSION 1 - EXECUTION 2 de Interclasser([8], [])
# je rentre dans le if len(tab2) == 0:
# je retourne tab1
# je retourne [8]


# RETOUR EXECUTION 1 de interclasser([8], [3])
# je suis maintenant fixé sur la valeur de interclasser([8], [])
# je return donc [3] + [8] => [3, 8]



# RETOUR RECURSION 1.1 - EXECUTION 2.1 - triFusion([8,3])
# le return interclasser(triFusion([8]), triFusion([3])) vaut [3, 8] !!



# RECURSION 1.2 - EXECUTION 2.2 - triFusion([5, 1])
# if len(tab) <= 1: => if 2 <= 1, cette condition renvoie false
# half_tab = len(tab) //2 => 2//2 => 1
# on passe au return interclasser(triFusion(tab[:half_tab]), triFusion(tab[half_tab:]))
# return interclasser(triFusion(tab[:1]), triFusion(tab[1:]))
# return interclasser(triFusion([5]), triFusion([1]))


# RECURSION 1.2.1 - EXECUTION 2.2.1 - triFusion([5])
# if len(tab) <= 1: => if 1 <=1, cette condition renvoie true
# on retourne tab => on retourne [5]

# RECURSION 1.2.2 - EXECUTION 2.2.2 - triFusion([1])
# if len(tab) <= 1: => 1 <= 1, cette condition renvoie true
# on retourne tab => on retourne [1]


# RETOUR RECURSION 1.2 - EXECUTION 2.2 - triFusion([5,1])
# je suis maintenant fixé sur la valeur de triFusion([5]), et triFusion([1])
# je vais pouvoir executer la fonction interclasser([5], [1])

# EXECUTION 1 de interclasser([5], [1])
# je ne rentre dans aucun des deux ifs  if len(tab1) == 0: et  if len(tab2) == 0:
# if tab1[0] < tab2[0]:
# if 5 < 1, cette condition renvoie false
# on passe dans le else
# return [tab2[0]] + interclasser(tab1, tab2[1:])
# return [1] + interclasser(5, [])

# RECURSION 1 - EXECUTION 2 de interclasser([5], [])
# if len(tab2) == 0:, je rentre dans ce if, je return tab1 => [5]

# RETOUR EXECUTION 1  de interclasser([5], [1])
# maintenant je sais ce que vaut interclasser(5, []) => [5]
# je peux retourner la valeur de interclasser([5], [1])
# c'est donc [1] + [5] => [1,5]

# RETOUR RECURSION 1.2 - EXECUTION 2.2 - triFusion([5,1])
# j'ai éxecuté interclasser([5], [1]), je sais donc ce que vaut triFusion(5,1) => [1,5]

# RETOUR EXECUTION 1 de triFusion([8, 3, 1, 5])

# je suis maintenant fixé sur les valeurs des paramètres que je vais envoyer à la fonction interclasser !
# triFusion([8, 3]) vaut [3, 8] et triFusion([5, 1]) vaut [1, 5]
# donc j'éxecute interclasser([3,8], [1,5])

# EXECUTION 1 de interclasser ([3,8], [1,5])
# on ne rentre dans aucun des deux ifs if len(tab1) == 0: et if len(tab2) == 0:
# if tab1[0] < tab2[0]:
# if 3 < 5, cette condition retourne true, je retourne
# return [tab1[0]] + interclasser(tab1[1:], tab2)
# return [3] + interclasser([8], [5, 1])

# RECURSION 1 - EXECUTION 2 de interclasser([8], [5, 1])
# on ne rentre dans  aucun des deux ifs if len(tab1) == 0: et if len(tab2) == 0:
# if tab1[0] < tab2[0]:
# if 8 < 5, cette condition renvoie false, je passe dans le else
# return [tab2[0]] + interclasser(tab1, tab2[1:])
# return [5] + interclasser([8], [1])

# RECURSION 2 - EXECUTION 3 de interclasser([8], [1])
# on ne rentre dans  aucun des deux ifs if len(tab1) == 0: et if len(tab2) == 0:
# if tab1[0] < tab2[0]:
# if 8 < 1, cette condition renvoie false, je passe dans le else
# return [tab2[0]] + interclasser(tab1, tab2[1:])
# return [1] + interclasser([8], [])

# RECURSION 3 - EXECUTION 4 de interclasser([8], [])
# on rentre dans le if len(tab2) == 0:
# return tab1 => [8]

# RETOUR RECURSION 2 - EXECUTION 3 de interclasser([8], [1])
# je suis fixé maintenant sur la valeur de interclasser([8], []) => [8]
# je retourne [1] + [8] => [1,8]

# RETOUR RECURSION 1 - EXECUTION 2 de interclasser([8], [5, 1])
# je suis maintenant fixé sur la valeur de interclasser([8], [1]) => [1,8]
# je retourne [5] + [1,8] => [5, 1, 8]

# RETOUR EXECUTION 1 de interclasser([3,8], [5,1])
# je suis maintentant fixé sur la valeur de interclasser([8], [5, 1])
# je return [3] + [5, 1, 8] => [3, 5, 1, 8]


test_concat = [5] + [1, 8]

print("test concat", test_concat)



# Exercice 3 : Tri par Fusion (nlogden) (2 e essai)


tab_test_tri_fusion_2 = [7, 2, 6, 1]


def interclasser_2(tab1, tab2):
    if len(tab1) == 0:
        return tab2
    if len(tab2) == 0:
        return tab1
    if tab1[0] <= tab2[0]:
        return [tab1[0]] + interclasser_2(tab1[1:], tab2)
    else:
        return [tab2[0]] + interclasser_2(tab1, tab2[1:])



def triFusion2(tab):
    if len(tab) <= 1:
        return tab
    slice_index = len(tab) // 2
    return interclasser_2(triFusion2(tab[:slice_index]), triFusion2(tab[slice_index:]))



print("test de trifusion 2",triFusion2(tab_test_tri_fusion_2))


print("test de tab_test_tri_fusion_2 [:2]", tab_test_tri_fusion_2[:2])

print("test de tab_test_tri_fusion_2 [2:]", tab_test_tri_fusion_2[2:])



# Décomposition - execution à la main de triFusion2 avec tab_test_tri_fusion_2 en paramètre
# (on appelera triFusion2 => triFusion et interclasser_2 =>  interclasser pour simplifier)

# EXECUTION 1 de triFusion([7, 2, 6, 1])
# je vérifie si le tableau ne contient qu'un élément
# if len(tab) <= 1:
# if 4 <= 1, cette condition renvoie false, je ne rentre pas le if et je continue
# slice_index = len(tab) // 2
# slice_index = 4 // 2 => 2
# je retourne l'appel de la fonction interclasser en lui passant en paramètres deux éxecutions de triFusion
# return interclasser(triFusion(tab[:slice_index]), triFusion(tab[slice_index:]))
# return interclasser(triFusion(tab[:2]), triFusion(tab[2:]))
# return interclasser(triFusion([7, 2]), triFusion([6, 1]))
# je me vois dans l'impossibilité d'executer interclasser, puisque je ne connais pas la valeur de ses paramètres
# je vais donc commencer par calculer la valeur des deux paramètres d'interclasser (triFusion([7, 2]), triFusion([6, 1]))

# RÉCURSION 1.1 - EXECUTION 2.1 triFusion([7, 2])
# if len(tab) <= 1:
# if 2 <= 1: cette condition renvoie false
# je passe à la suite je ne rentre pas dans le if
# slice_index = len(tab) // 2 => 2//1 => 1
# return interclasser(triFusion(tab[:slice_index]), triFusion(tab[slice_index:]))
# return interclasser(triFusion([7]), triFusion([2]))

# RÉCURSION 1.1.1 - EXECUTION 2.1.1 triFusion([7])
# if len(tab) <= 1: => if 1 <= 1, cette condition renvoie true, je je return tab
# triFusion([7]) => [7]

# RÉCURSION 1.1.2 - EXECUTION 2.1.2 triFusion([2])
# if len(tab) <= 1: => if 1 <= 1, cette condition renvoie true, je je return tab
# triFusion([2]) => [2]

# RETOUR RÉCURSION 1.1 - EXECUTION 2.1 triFusion([7, 2])
# je suis maintenant fixé sur deux choses dont j'avais besoin pour executer ma fonction interclasser
# ces deux choses me manquaient : triFusion([7]), triFusion([2])
# je peux donc retourner interclasser([7], [2])

# EXECUTION 1 - interclasser([7], [2])
# Je ne rentre dans aucun des ifs if len(tab1) == 0: if len(tab2) == 0:
# if tab1[0] <= tab2[0]: => if 7 <= 2, cette condition renvoie false, je passe dans le else
# return [tab2[0]] + interclasser(tab1, tab2[1:])
# return [2] + interclasser([7], [])
# je ne connais la valeur de interclasser([7], []), donc je vais l'executer

# RÉCURSION 1 - EXECUTION 2 - interclasser([7], [])
# je rentre dans le if len(tab2) == 0: => if 0 == 0
# je return tab1
# je return [7]

# RETOUR EXECUTION 1 - interclasser([7], [2])
# Je suis maintenant fixé sur la valeur de interclasser([7], [])
# c'est [7]
# donc je return [2] + [7] => [2, 7]


# RETOUR RÉCURSION 1.1 - EXECUTION 2.1 triFusion([7, 2])
# je peux retourner interclasser([7], [2]),
# qui vaut [2, 7]
# Cette étape signe la fin de la première grosse branche

# RÉCURSION 1.2 - EXECUTION 2.2 - triFusion([6, 1])
# if len(tab) <= 1: => if 2 <= 1
# cette condition renvoie false, je ne rentre pas dans ce if
# slice_index = len(tab) // 2
# slice_index = 2 //2 => 1
# return interclasser(triFusion(tab[:slice_index]), triFusion(tab[slice_index:]))
# return interclasser(triFusion([6]), triFusion([1]))
# je connais pas la valeur des paramètres de interclasser, donc je vais les calculer

# RÉCURSION 1.2.1 - EXECUTION 2.2.1 - triFusion([6])
# if len(tab) <= 1: => if 1 <= 1, cette condition renvoie true
# je rentre dans le if, je return tab => [6]

# RÉCURSION 1.2.2 - EXECUTION 2.2.2 - triFusion([1])
# if len(tab) <= 1 => if 1 <= 1, cette condition renvoie tru
# je rentre dans le if, je return tab => [1]

# RETOUR RÉCURSION 1.2 - EXECUTION 2.2 - triFusion([6, 1])
# je suis maintenant fixé sur la valeur des deux paramètres que j'envoie à interclasser triFusion([6]), triFusion([1])
# je peux exécuter ma fonction interclasser([6], [1])


# EXECUTION 1 - interclasser([6], [1])
# je ne rentre dans aucun des deux ifs if len(tab1) == 0: if len(tab2) == 0:
# if tab1[0] <= tab2[0]:
# if 6 <= 1, cette condition renvoie false
# je passe dans le else
# return [tab2[0]] + interclasser(tab1, tab2[1:])
# return [1] + interclasser([6], [])
# je constate que je connais pas la valeur de interclasser([6], []), je vais donc devoir la calculer...

# RÉCURSION 1 - EXECUTION 2 interclasser([6], [])
# je rentre dans le if len(tab2) == 0: (le 2 e tableau est vide)
# je return tab1 => je return [6]

# RETOUR EXECUTION 1 - interclasser([6], [1])
# je suis maintenant fixé sur la valeur de interclasser([6], []) => [6]
# je peux donc retourner [1] + [6] => [1,6]

# RETOUR RÉCURSION 1.2 - EXECUTION 2.2 - triFusion([6, 1])
# je suis maintenant fixé sur la valeur de interclasser([6], [1])
# je retourne [1, 6]
# Cette étape signe la fin de la deuxième grosse branche

# RETOUR EXECUTION 1 de triFusion([7, 2, 6, 1])
# je connais désormais les valeurs des paramètres que je vais envoyer à interclasser(triFusion([7, 2]), triFusion([6, 1]))
# interclasser([2, 7], [1, 6])

# EXECUTION 1 - interclasser([2,7], [1, 6])
# je ne rentre dans aucun des deux ifs
# if len(tab1) == 0:  if len(tab2) == 0: => if 2 == 0 => if 2 == 0
# if tab1[0] <= tab2[0]:
# if 2 <= 1, cette condition renvoie false
# je passe dans le else
# return [tab2[0]] + interclasser(tab1, tab2[1:])
# return [1] + interclasser([2, 7], [6])
# je ne connais pas la valeur de interclasser([2, 7], [6]), je vais donc la calculer

# RÉCURSION 1 - EXECUTION 2 - interclasser([2, 7], [6])
# je ne rentre dans aucun des deux ifs
# if len(tab1) == 0: if len(tab2) == 0 => if 2 == 0 if 1 == 0
# if tab1[0] <= tab2[0]:
# if 2 <= 6, cette condition renvoie true
# je rentre dans ce bloc if
# return [tab1[0]] + interclasser(tab1[1:], tab2)
# return [2] + interclasser([7], [6])
# je ne connais pas la valeur de interclasser([7], [6]), je vais donc la calculer


# RÉCURSION 2 - EXECUTION 3 - interclasser([7], [6])
# je ne rentre dans aucun des deux ifs
# if len(tab1) == 0: if len(tab2) == 0 if 1 == 0 if 1 == 0
# if tab1[0] <= tab2[0]:
# if 7 <= 6
# cette condition renvoie false
# je passe dans le else
# return [tab2[0]] + interclasser(tab1, tab2[1:])
# return [6] + interclasser([7], [])
# je ne connais pas la valeur de interclasser([7], []) je vais donc la calculer

# RÉCURSION 3 - EXECUTION 4 - interclasser([7], [])
# if len(tab2) == 0: if 0 == 0, je rentre dans ce if
# je return return tab1 => [7]

# RETOUR RÉCURSION 2 - EXECUTION 3 - interclasser([7], [6])
# je suis maintenant fixé sur la valeur de interclasser([7], []) => [7]
# je return [6] + [7] => [6,7]

# RETOUR RÉCURSION 1 - EXECUTION 2 - interclasser([2, 7], [6])
# je suis maintenant fixé sur la valeur de interclasser([7], [6]) => [6, 7]
# je return [2] + [6, 7] => [2, 6, 7]

# RETOUR EXECUTION 1 - interclasser([2,7], [1, 6])
# je suis maintenant fixé sur la valeur de interclasser([2, 7], [6]) => [2, 6, 7]
# je return [1] + [2, 6, 7] => [1, 2, 6, 7]

# RETOUR EXECUTION 1 de triFusion([7, 2, 6, 1])
# je devais retourner interclasser([2, 7], [1, 6])
# j'ai calculé sa valeur et j'ai mon tableau trié => [1, 2, 6, 7]






# print("test de tab_test_tri_fusion_2 [2:]", tab_test_tri_fusion_2[2:])

# Exercice 4 : Tri Rapide (nlogden)

# Exercice 5 : Tri par Comptage (O(n)) https://info.blaisepascal.fr/nsi-complexite-dun-algorithme/

# Tu dois créer comme un dictionnaire ou chaque clé est un entier naturel
# et chaque valeur,me nb de fois que cette clé est trouvée dans le tableau à trier

dico_comptage = {
    0: []
}

tab_test_tri_comptage = [32, 78, 78, 12, 11, 11, 11, 23, 9, 9, 9, 9, 3, 2, 1, 1]

tab_unsorted = [randint(0,100) for _ in range(50)]

def count_sort(tab:list):
    max = tab[0]
    for v in tab:
        if v > max:
            max = v
    lcount = [0] * (max + 1)
    for v in tab:
        lcount[v] +=1
    tab.clear()
    for k, v in enumerate(lcount):
        tab += [k] * v
    return tab


print("Test du tableau avant le tri par comptage \n", tab_unsorted)


count_sort(tab_unsorted)

print("Test du tableau après le tri par comptage \n", tab_unsorted)



# Exercice 6 : Tri par insertion (quadratique)

# placer l'élément le plus petit vers le début du tableau.

# je parcours le tableau, des que je trouve un élément plus petit que le minimum je le place en décalant tout le reste



tab_test_tri_par_insertion = [43, 41, 2, 8, 1, 12, 1]


def insert_sort(tab):
    for i in range(1, len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] >= x:
            tab[j] = tab[j -1]
            j -=1

        tab[j] = x


print("test du tri par insertion avant INSERT SORT \n", tab_test_tri_par_insertion)

insert_sort(tab_test_tri_par_insertion)

print("test du tri par insertion après INSERT SORT \n", tab_test_tri_par_insertion)


# Tri par insertion execution avec l'exemple d'un tableau à 4 éléments tab_insert = [3, 1, 8, 5]


# EXECUTION insert_sort([3, 1, 8, 5])


# TOUR DE BOUCLE n 1 de i (i = 1 car i commence à 1, et termine à len(tab), donc 4, et on s'arrêtera un cran avant donc à 3)
# x = tab[i] => x = 1
# j = i => j = 1


# TOUR WHILE n 1 (j>0 => 1 >0, cette condition renvoie true,  tab[j-1] >= x => tab[0] >= x => 3 >= 1, cette condition renvoie true aussi)
# tab[j] = tab[j -1] => tab[1] = tab[0] => tab[1] = 3
# ici le tableau vaut donc [3, 3, 8, 5]
# j -=1 => 1 -= 1 => j = 0 !
# dernier tour de boucle WHILE

# tab[j] = x => tab[0] recoit 1. Le tableau à cette étape est donc [1, 3, 8, 5]


# TOUR DE BOUCLE n2  de i (i = 2 (avant dernier tour))
# x = tab[i]
# j = i



# TOUR WHILE n1 (j > 0 and tab[j-1] >= x: => )




# Exercice 7 : Tri par séléction (quadratique)

tab_test_tri_selection = [34, 2, 89, 21, 3]

def select_sort(tab):
    for i in range(len(tab) -1):
        min = i
        for j in range(i, len(tab)):
            if tab[j] < tab[min]:
                min = j
        permutation(tab, i, min)





print(" test du tableau tri selection avant la fonction de selection \n", tab_test_tri_selection)

select_sort(tab_test_tri_selection)

print(" test du tableau tri selection après la fonction de selection \n", tab_test_tri_selection)

tab_test_tri_selection = [34, 2, 3, 21, 89]

def select_sort3(tab):
    i = 0
    is_sorted = False
    while not is_sorted and i < len(tab) -1:
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        if min != i:
            tab[min], tab[i] = tab[i], tab[min]
        else:
            is_sorted = True
        i +=1


print(" test du tableau tri selection avant la fonction de selection 3 \n", tab_test_tri_selection)

select_sort3(tab_test_tri_selection)

print(" test du tableau tri selection après la fonction de selection 3 \n", tab_test_tri_selection)

# permutation(tab_test_tri_selection, 0, 1)

# print(tab_test_tri_selection)


# Exercice 8 : Tri par séléction avec tests d'égalité (quadratique)

# Exercice 9 : Tri à bulle (quadratique)


tab_test_tri_a_bulle = [1900,400932, 28989992, 3, 78, 31, 12, 12, 999, 900, 123]

def bubble_sort(tab):
    for i in range(len(tab) -1):
        for j in range(len(tab) - i - 1):
            if tab[j] > tab[j + 1]:
                permutation(tab, j, j + 1)

print(tab_test_tri_a_bulle)

bubble_sort(tab_test_tri_a_bulle)

print("test de l'algo bubble sort ", tab_test_tri_a_bulle)



# Execution main pour comprendre le tri à bulle


# tableau d'exemple tab_bubble_ex = [32, 12, 90, 4]

# EXECUTION FONCTION bubble_sort(tab) bubble_sort([32, 12, 90, 4, 2])

# TOUR DE BOUCLE numéro 1 de i (i = 0) (on ira jusqu'à i = 4, car len(tab) = 5 et on s'arrête un cran avant)


# TOUR DE BOUCLE numéro 1 de j (j = 0) (borne max ici 5 - 0 - 1 => 4 (on s'arrêtera à j = 3 ducou))
# if tab[j] > tab[j + 1]:
# if tab[0] > tab[1]:
# if 32 > 12 => cette condition renvoie true, je rentre dans le if
# permutation(tab, j, j + 1) => permutation([32, 12, 90, 4, 2], 0, 1) => l'élément 0 et l'élément 1 du tableau vont être inversés
# à ce stade, tab_bubble_ex = [12, 32, 90, 4, 2]

# TOUR DE BOUCLE numéro 2 de j (j = 1)
# if tab[j] > tab[j + 1]:
# if tab[1] > tab[2]: => 32 > 90, cette condition renvoie false, on ne rentre pas dans le if, on passe au tour suivant

# TOUR DE BOUCLE numéro 3 de j (j =2)
# if tab[j] > tab[j + 1]:
# if tab[2] > tab[3]: if 90 > 4 =>  cette condition renvoie true, on rentre dans le if
# permutation(tab, j, j + 1) => permutation([12, 32, 90, 4, 2], 2, 3) => l'élément 2 et 3 du tableau vont être inversés
# à ce stade, tab_bubble_ex = [12, 32, 4, 90, 2]

# TOUR DE BOUCLE numéro 4 de j (j = 3), ce tour sera notre dernier !
# if tab[j] > tab[j + 1]: => if tab[3] > tab[4]: => 90 > 2
# cette condition renvoie true, om rentre dans le if
# permutation(tab, j, j + 1) => permutation([12, 32, 4, 90, 2], 3, 4)
# l'élément 3 et 4 du tableau vont être permutés, le nouveau tableau est => [12, 32, 4, 2, 90]
# fin des boucles j.


# TOUR DE BOUCLE numéro 2 de i (i = 1) (on ira jusqu'à i = 4, car len(tab) = 5 et on s'arrêtera un cran avant)


# TOUR DE BOUCLE numéro 1 de j (j = 0) (borne max ici 5 - 1 -1  = 3, donc on s'arrêtera à j = 2)
# if tab[j] > tab[j + 1]: =>  if tab[0] > tab[1]:
# => if 12 > 32, cette condition renvoie false, on ne rentre pas dans le if

# TOUR DE BOUCLE numéro 2 de j (j = 1)
# if tab[j] > tab[j + 1]: => if[tab[1] > tab[2]: => if 32 > 4, cette condition renvoie true
# je rentre dans le if
# permutation(tab, j, j + 1) => permutation([12, 32, 4, 2, 90], 1, 2), les éléments en position 1 et 2 du tableau vont être permutés
# le tableau ici sera [12, 4, 32, 2, 90]

# TOUR DE BOUCLE numéro 3 de j (j = 2) (dernier tour)
# if tab[j] > tab[j + 1]: => if tab[2] > tab[3] => if 32 > 2, cette condition renvoie true,
# je rentre dans le if
# permutation(tab, j, j + 1) => permutation([12, 4, 32, 2, 90], 2, 3), les éléments en position 2 et 3 du tableau vont être permutés
# le tableau est désormais [12, 4, 2, 32, 90]
# fin des boucles j


# TOUR DE BOUCLE numéro 3 de i (i = 2) (on ira jusqu'à i = 4 (len(tab) = 5))


# TOUR DE BOUCLE numéro 1 de j (j = 0) (borne max ici 5 - 2- 1 = 2, donc on s'arrêtera à j = 1)
# if tab[j] > tab[j + 1]: => if tab[0] > tab[1]: => if 12 > 4, cette condition renvoie true,
# je rentre dans le if
# permutation(tab, j, j + 1) => permutation([12, 4, 2, 32, 90], 0, 1), les éléments 0 et 1 du tableau vont être inversés
# [4, 12, 2, 32, 90]

# TOUR DE BOUCLE numéro 2 de j (j =1) (dernier tour)
# if tab[j] > tab[j + 1]: => if tab[1] > tab[2]: => if 12 > 2, cette conditon renvoie true,
# je rentre dans le if
# permutation(tab, j, j+ 1) => permutation([4, 12, 2, 32, 90], 1, 2), les éléments 1 et 2 du tableau vont être inversés
# [4, 2, 12, 32, 90]
# fin des boucles j


# TOUR DE BOUCLE numéro 4 de i (i = 3)

# TOUR DE BOUCLE numéro 1 de j (j=0) (borne max ici 5 - 3 -1 => 1, donc on s'arrête à j = 0) (déjà dernier tour)
# if tab[j] > tab[j + 1]: => if tab[0] > tab[1] => if 4 > 2, cette condition renvoie true, je rentre dans le if
# permutation(tab, j, j+ 1) => permutation([4, 2, 12, 32, 90], 0, 1), les éléments 0 et 1 du tableau vont être inversés
# [2, 4, 12, 32, 90]
# fin des boucles j

# TOUR DE BOUCLE numéro 5 de i (i =4) (dernier tour)


# ON NE PEUT PAS RENTRER DANS LA BOUCLE J => len(tab) - i - 1 => 5 - 4 - 1 => 0, le début c'est 0 et à la fin c'est zéro donc on
# ne peut pas rentrer dans la boucle j sur ce tour de boucle i et le tableau est [2, 4, 12, 32, 90], donc il est trié !











# Suite (à part, code batard exécuté à la main)

# to_permute = [190, 89, 2, 3]
# permutation(to_permute, 0, 1)
# print(to_permute)


# Execution du code à la main, décomposition avec un tableau à 4 éléements tab_bubble = [190, 89, 2, 3]

# EXECUTION select_sort(tab) => select_sort([190, 89, 2, 3])

# TOUR DE BOUCLE de i 1 (i = 0) for i in range(len(tab) -1): => for i in range(3) (i s'arrête un cran avant le chiffre du range donc il vaudra 0, 1, 2)

# TOUR DE BOUCLE de j 1 (j = i + 0 => j = 0) (j partira de i, jusqu'à 3, donc au début j vaut 0, puis 1, puis 2, puis 3)
# if tab[i] > tab[j]: => if tab[0] > tab[0] => if 190 > 190 => cette condition renvoie false, on ne rentre pas dans le if
# TOUR DE BOUCLE de j 2 (j =i +1 => j = 1)
# if tab[i] > tab[j]: => if tab[0] > tab[1] => if 190 > 89 => cette condition renvoie true, on rentre dans le if
# permutation(tab, i, j) => permutation([190, 89, 2, 3], 0, 1) => [89, 190, 2, 3]
# TOUR DE BOUCLE j 3 (j =i + 2 => j = 2)
# if tab[i] > tab[j]: if tab[0] > tab[2]: => if 89 > 2 => cette condition renvoie true, on rentre dans le if
# permutation(tab, i, j) => permutation([89, 190, 2, 3], 0, 2) => [2, 190, 89, 3]
# TOUR DE BOUCLE j 4 (j = i+3 => j = 3)
# if tab[i] > tab[j]: if tab[0] > tab[3] => if 2 > 3 => cette condition renvoie false, je ne rentre pas dans le if
# j = 3 (1 cran en dessous du range(4)), je m'arrête. tableau = [2, 190, 89, 3] à ce stade

# TOUR DE BOUCLE i 2 (i = 1)

# TOUR DE BOUCLE de j 1 (j = i + 0 => 1 + 0 => j = 1)
# if tab[i] > tab[j]: => if tab[1] > tab[1]: => if 190 > 190, cette condition renvoie false, je ne rentre pas dans le if
# TOUR DE BOUCLE j 2 (j = i + 1 => 1 + 1 => j = 2)
# if tab[i] > tab[j]: => if tab[1] > tab[2]: if 190 > 89, cette condition renvoie true, je rentre dans le if
# permutation(tab, i, j) => permutation([2, 190, 89, 3], 1, 2) => [2, 89, 190, 3]
# TOUR DE BOUCLE j 3 (j = i + 2 => 1 + 2 => j = 3), ce sera d'ailleurs le dernier tour de boucle j dans le contexte de cette boucle i
# if tab[i] > tab[j]: => if tab[1] > tab[3]: => if 190 > 3, cette condition renvoie true, je rentre dans le if
# permutation(tab, i, j) => permutation([2, 89, 190, 3], 1, 3) => [2, 3, 190, 89]
# fin des tours de boucle j. j =3, on s'arrête un cran avant la fin du chiffre max du range (qui vaut 4 ici (len(tab)))

# TOUR DE BOUCLE i 3 (i = 2) (précisons que ce sera le dernier tour de boucle i, on s'arrete un cran avant la borne maximale du range qui est len(tab) -1  => 4 - 1 => 3)

# TOUR DE BOUCLE j 1 (j = i + 0 => 2 + 0 => j = 2)
# if tab[i] > tab[j]: =>  if tab[2] > tab[2] => if 190 > 190, cette condition renvoie false, je ne rentre pas dans le if
# TOUR DE BOUCLE j 2 (j = i + 1 => 2 + 1 => j = 3), dernier tour de boucle j
# if tab[i] > tab[j]: => if tab[2] > tab[3] => if 190 > 89, cette condition renvoie true, je rentre dans le if
# permutation(tab, i, j) => permutation([2, 3, 190, 89], 2, 3) => [2, 3, 89, 190]

# fin des deux tours de boucle, tableau trié ! tab_bubble = [2, 3, 89, 190]



# Exerice 10 : comparer tous les types de tris
