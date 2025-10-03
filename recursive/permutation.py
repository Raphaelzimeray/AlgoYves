# Ecrire une fct récursive retournant la liste de toutes les permutations possibles d'une liste**

list_example = [1, 2, 3, 6, 2, 4, 89, 31, 33, 400]

# liste de toutes les permutations possibles de [2,3,4]
# [234, 243, 324, 342, 423, 432] je connais ca. Comment faire pour une liste avec un élément de plus à gauche
# pour avoir toutes les permutations qui commenceraient par le 1
# [1234, 1243, 1324...]
# Liste des permutations possibles de 134
# [134, 143, 314, 341, 413, 431]
# Toutes les permutations possibles qui commencent par un 2 il faut rajouter un 2 à gauche
# [2134, 2143, 2314, 2341, 2412, 2431]
# Idem pour le 3, idem pour le 4
# la concaténation des 4 listes me donne les listes possibles.
# je boucle avec un itérateur sur la longueur de la liste

def permutation_rec(l):
    if len(l) == 1:
        return [l]
    if len(l) == 0:
        return []
    permutations_finals = []
    for i in range (len(l)):
        current_value = l[i]
        list_remain = l[:i] + l[i+1:]
        # je considère que je connais toutes les permutations de la liste remaim
        # je considère que je connais la ligne 6
        # je vais parcourir la liste de l'ensemble des permutations
        for lp in permutation_rec(list_remain):
            permutations_finals.append([current_value] + lp)


    return permutations_finals


print("test de permutation rec")
perm = permutation_rec(list_example)
for p in perm:
    print(p)
print(len(perm), "permutations")

# Analyse du code avec [1, 2, 3] en paramètres.
# Valeur attendue en sortie:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]

# EXECUTION 1 On rentre la fonction perm_rec([1,2,3])
# on est pas dans les cas d'arret len(l) == 1 et len(l) == 0
# on déclare permutation_finals = [], qui sera la liste de liste qui sera retournée à la fin
# ensuite for i in range (len(l)): on itère sur la longeur de la liste avec un i qui va aller de 0 à 2
# ici itérateur i = 0
# current_value recoit l[i], première itération l[0], c'est à dire 1. current_value = 1
# on déclare list_remain qui recoit l[:0] (je commence du début et je marrête avant l'indice final qui est l'indice 0) + l[0+1:]
# ( ce qui veut dire je commence à l'index 1 et je vais jusqu'à la fin de la liste)
# list remain = [] + [2, 3] => [2,3]
# je crée une nouvelle itération

def factoriel(n):
    if n <= 1:
        return 1
    else:
        return n * factoriel(n-1)

print(factoriel(10))
