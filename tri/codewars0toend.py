# Moving 0s to the end


def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            for j in range(len(lst) -i):
                lst[j+i] = lst[j+i+1]
            lst[-1] = 0

    return lst


# tableau test tab_test = [1, 0, 1, 2, 0, 1, 3]
# est censé retourner [1, 1, 2, 1, 3, 0, 0]
# décomposition du code pour corriger l'erreur "list assignment index out of range"

# TOUR DE BOUCLE 1 de I ou i = 0 (i va de 0 à len(lst) -1(7), donc le i va de 0 à 6, ce qui fera 7 tours de boucle au total)
# if lst[i] == 0:
# if lst[0] == 0:
# if 1 == 0:, cette condition renvoie false, je passe au tour de boucle suivant

# TOUR DE BOUCLE 2 DE I ou i = 1
# if lst[i] == 0:
# if lst[1] == 0:
# if 0 == 0:
# cette condition renvoie true,
# je rentre dans la boucle J
# TOUR DE BOUCLE 1 de J ou j = 0(j va de 0 à len(lst) -1(6), donc le j va de 0 à 5, ce qui fera 7 tours de boucle au total)
# lst[j+i] = lst[j+i+1]
# lst[0+1] = lst[0+1+1]
# lst[1] = lst[2]
# lst[1] = 1
# tableau à ce stade [1, 1, 1, 2, 0, 1, 3]
# TOUR DE BOUCLE 2 de J ou j = 1 et i = 1
# lst[j+i] = lst[j+i+1]
# lst[1+1] = lst[1+1+1]
# lst[2] = lst[3]
# lst[2] = 2
# tableau à ce stade [1, 1, 2, 2, 0, 1, 3]
# TOUR DE BOUCLE 3 de J ou j = 2 et i = 1
# lst[j+1] = lst[j+i+1]
# lst[2+1] = lst[2 + 1 + 1]
# lst[3] = lst[4]
# lst[3] = 0
# tableau à ce stade [1, 1, 2, 0, 0, 1, 3]




# tab_test = [1, 0, 1, 2, 0, 1, 3]

# tab_test[1] = tab_test[2]
# tab_test[-1] = 0

# print(tab_test)



# def move_zeros(lst):
#     for i in range(len(lst)):
#         if lst[i] == 0:
#             for j in range(i, len(lst) -i):
#                 lst[j] = lst[j+i]
#             lst[-1] = 0

#     return lst


# print("test de move zeros", move_zeros(tab_test))

# test avec un tableau de toute petite taille = [1, 0, 3, 0, 1]
# je voudrai obtenir [1, 3, 1, 0, 0]

# TOUR DE BOUCLE 1 de i (i = 0)
# if lst[i] == 0:
# if lst[0] == 0:
# if 1 == 0: cette condition renvoie false je passe au 2 e tour de boucle
# TOUR DE BOUCLE 2 de i (i = 1)
# if lst[i] == 0:
# if lst[1] == 0:
# if 0 == 0: cette condition renvoie true je rentre en ligne 63 dans la boucle for j
#
# TOUR DE BOUCLE 1 de j (j = i)
# lst[j] = lst[j+1]
# lst[1] = lst[1+1]
# lst[1] = lst[2]
# lst[1] = 3
# tableau à ce stade [1, 3, 3, 0, 1]

# TOUR DE BOUCLE 2 de j (j = i + 1 => 2)
# lst[j] = lst[j+1]
# lst[2] = lst[2 + 1]
# lst[2] = lst[3]
# lst[2] = 0
# lst[2] = 0
# tableau à ce stade [1, 3, 0, 0, 1]

# TOUR DE BOUCLE 3 de j (j = i + 2 => 3)
# lst[j] = lst[j+1]
# lst[3] = lst[3 +1]
# lst[3] = lst [4]
# lst[3] = 1
# tableau à ce stade [1, 3, 0, 1, 1]

# à ce stade on a déjà un soucis c'est qu'on a perdu un des 0. Il faut donc corriger le code de sorte à ce que
# les zéros apparaissent au fond

# une autre solution plus simple serai de stocker dans un tableau temporaire chaque zéro que l'on croise,
# stocker dans un autre tableau temporaire tous les chiffres qui ne sont pas des zéros
# et concaténer les deux à la fin

tab_test = [1, 0, 1, 2, 0, 1, 3]

def move_zeros(lst):
    tab_zeros = []
    tab_not_zeros = []
    for i in range(len(lst)):
        if lst[i] == 0:
            tab_zeros.append(lst[i])
        else:
            tab_not_zeros.append(lst[i])
    print(tab_zeros)
    print(tab_not_zeros)
    joined_tab = tab_not_zeros + tab_zeros
    return joined_tab

move_zeros(tab_test)

print("test de la fonction move zeros ", move_zeros(tab_test))


# ok tout marche !


# Version avec pop et append

def move_zeros_2(lst):
    print(lst)
    k = len(lst)-1
    i = 0
    while i < k:
        if lst[i]==0:
            lst.pop(i)
            lst.append(0)
            k -= 1
        print(lst)
        if lst[i] != 0:
            i+=1
    return lst


def move_zeros_3(lst:list):
    # return [n for n in lst if n != 0]+ [n for n in lst if n == 0]
    return [n for n in lst if n != 0]+ [0] * lst.count(0)


# Créer des listes en python. Je sais afficher les éléments de 0 à 10
tab_test = [1, 0, 1, 2, 0, 1, 3]


l1 = [i for i in tab_test if i != 0]
print(l1)
l2 = [i for i in tab_test if i == 0]
print(l2)
l3 = l1 + l2
print(l3)
l4 = [0] * 5
print(l4)


# Sort the odd

def sort_array(source_array):
    print(source_array)
    odd_list = [i for i in source_array if i %2 != 0]
    odd_list.sort()
    for k, v in enumerate(source_array):
        if v%2 != 0:
            source_array[k] = odd_list.pop(0)
    return source_array
