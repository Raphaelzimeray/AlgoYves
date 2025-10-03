from random import randint
from time import sleep


# Exercice 1 : je fourni en paramètre deux années croisantes, et je veux que ca affiche les années qui vont de l’une à l’autre.
# Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.

def print_years_rec(year1, year2):
    if year2 < year1:
        print("Terminé")
    else:
        print(year1)
        return print_years_rec(year1 + 1, year2)

print(print_years_rec(2012, 2019))

# ok

# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n.


def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p-1)


print(power_rec(5, 10))

# ok, pourquoi il n'y a pas trop de récursions?


# Exercice 3 : Le nombre de chiffre d’un nombres. 1970 => 4


def count_digits(num):
    if num <=0:
        return 0
    else:
        return 1 + count_digits(num//10)


print("test de count digits", count_digits(88888888888))

# ok

# Exercice 4 : la somme des chiffres d’un nombre. 1970 = 1+9+7+0.


def sum_of_digits(num):
    if num <=1:
        return 0
    else:
        return num%10 + sum_of_digits(num//10)


print("test de sum digits", sum_of_digits(902011))

# ok question => Pourquoi il y a une erreur quand je fais parfois des additions dans les returns ?


# Exercice 5 : Afficher le chiffre de fibonacci

# Implémentation de l'algo. Je connais l'étape n -1, je peux donc connaitre l'étape n
# je sais que fib(0) = 0, et fib(1) = 1
# Donc, je sais que l'étape actuelle () = l'addition de l'étape d'avant (n-1) + de l'étape d'encore d'avant (n-2)
# je retourne donc la somme de l'appel des deux fonctions avec respectivement n-1 et n-2 en paramètres


def print_fib_rec(n):
    if n<=1:
        return n
    else:
        return print_fib_rec(n -1) + print_fib_rec(n -2)


print(print_fib_rec(7))

# ok

# Exercice 6 : Optimiser le temps de calcul avec un dictionnaire temporaire


# je dois prendre en compte que plus le chiffre en entrée est grand, et plus le nombre d'arbres evolue de manière exponentielle
# pour éviter de répéter des calculs dont on a déjà la réponse, on doit stocker l'information dans un dictionnaire temporaire (dico)
# Le dico prendra en valeur initial les valeurs de fib aux indices 0 et 1.

dico = {
    0: 0,
    1: 1
}

def print_fib_with_dico(n):
    if n not in dico:
        dico[n] = print_fib_with_dico(n -1) + print_fib_with_dico(n-2)
    return dico[n]


print(print_fib_with_dico(45))

# Exercice 7 : Code Wars : Reduce My Fraction


def get_pgcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == 1 or b == 1:
        return 1
    return get_pgcd(b%a, a)




def reduce_fraction(fraction):
    result = get_pgcd(fraction[0], fraction[1])
    return (fraction[0] / result, fraction[1] / result)

print("test de reduce my fraction", reduce_fraction((80, 120)))

# a faire en iteratif


# ok

# analyse du code en décomposé avec deux exemples : 45 / 120, 60/20.
# Exemple 1 (45/120).
# EXECUTION 1 get_pcdg(45, 120)=> ni a ni b ne sont = à 0 ou 1, donc on passe au return de la ligne 112.
# On return l'appel de la fonction get_pgcd(120%45, 45) => get_pgcd(30, 45)
# RECURSION 1, EXECUTION 2 get_pgcd(30, 45) => ni le a ni le b ne sont == à 0 ou 1, donc on passe au return de la ligne 112
# On return l'appel de la fonction get_pgcd(45%30, 30) => get_pgcd(15, 30)
# RECURSION 2, EXECUTION 3 get_pgcd(15, 30) => ni le a ni le b ne sont == à 0 ou 1, on passe au return de la ligne 112
# On return l'appel de la fonction get_pgcd(30%15, 15) => get_pgcd(0, 15)
# RECURSION 3, EXECUTION 4 get_pgcd(0, 15) => a == 0, on return b qui est égal à 15.
# 45 / 15 et 120 / 15 ca fait 3, 8. Résultat ok

# Exemple 2 (60/20)
# EXECUTION 1, get_pgcd(60, 120) => ni a ni b ne sont égaux à 0 ou 1, on passe dans le return de la ligne 122
# on return l'appel de la fonction get_pgcd(20%60, 60) => get_pgcd(20, 60)
# RECURSION 1, EXECUTION 2 => get_pgcd(20, 60) => ni le a ni le b ne sont égaux à 0 ou 1, on passe dans le return ligne 122
# on return l'appel de la fonction get_pgcd(60%20, 20) => get_pgcd(0, 20)
# RECUSION 2, EXECUTION 3 => get_pgcd(0, 20) a == 0, on return b (20).
# 60/20 et 20/20 => 3, 1. Résultat ok.











# Exercice 8 : Vérifier si un mot est un palindrome

# je déclare un tableau tab_test = ["radar", "retâter", "rêver", "bonjour", "python", "tôt", "kayak"]
# je sais que la condition d'arrêt de ma fonction c'est le moment ou le mot ne fait plus qu'une lettre, il n'y a alors plus rien à comparer
# je sais aussi que ce qui caractérise un palindrome, c'est que les lettres qui sont symétriquement opposées soient identiques
# donc cette condition qui renvoie true ou false doit être true pour qu'on passe à la suite, si à un moment donné,
# la lettre à l'index  donné est != de la lettre à l'index -1 -index, alors on sait que ce mot n'est pas un palindrome

tab_test = ["radar", "retâter", "rêver", "bonjour", "python", "tôt", "kayak", "cooc"]

def is_palindrome_rec(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] == word[-1] and is_palindrome_rec(word[1:-1])



for i in range(len(tab_test)):
    if is_palindrome_rec(tab_test[i]):
        print("le mot", tab_test[i], "est un palindrome")
    else:
        print("le mot", tab_test[i], "n'est pas un palindrome")



# Exercice 9 : Trouver le minimum d'un tableau

# condition d'arrêt (simialire à la condition while en itératif) => la taille du tableau est <= 1
# le plus petit élément c'est le plus petit élément entre le tableau[-1] et le dernier élément du tableau
# le plus petit élément du tableau est dans une variable min_tab_temporaire, qui va recevoir l'appel de la fonction récursive find_min_rec(tab[-1])
# les comparaisons auront lieu une fois qu'on commencera à remonter dans les poupées russes
# alors seulement le code des poupées russes s'executera et on aura en sortie sur la poupée parente le chiffre minimum du tableau


tab = [randint(0,100) for _ in range(20)]

def find_min_rec(tab):
    if len(tab) <= 1:
        return tab[0]
    else:
        min_tab_temporaire = find_min_rec(tab[:-1])
        if min_tab_temporaire < tab[-1]:
            return min_tab_temporaire
        else:
            return tab[-1]


print("le minimum du tableau", tab, "est: ", find_min_rec(tab))

# print(len(tab))

# Exemple de fonctionnement du code sur un tableau à 4 éléments. tab_example : [32, 9, 4, 11]
# EXECUTION 1 => def find_min_rec([32, 9, 4, 11]) recoit 4 éléments.
# la comparaison if len(tab) <= 1 renvoie false, on ne rentre donc pas dans ce if
# on passe dans le else => min_tab_temporaire recoit l'appel de la fonction récursive find_min_rec(tab[:-1]), c'est à dire
# le tableau moins le dernier élément. donc tab([32, 9, 4]). A ce moment la,
# la suite du code de la première fonction ne peut pas s'éxecuter, parce qu'on est en attente du résultat de find_min_rec(tab[:-1])
# pour que min_tab_temporaire puisse avoir une valeur et que les lignes suivantes s'executent

# RÉCURSION 1 - EXECUTION 2 => On rentre dans la première poupée russe, première récursivité avec le tableau à 4-1 éléments
# la comparaison if len(tab) <= 1  (4 <=1)renvoie false, on ne rentre donc pas dans ce if
# on passe dans le else => on déclare une variable min_tab_temporaire donc le scope est restreint à cette nouvelle fonction
# récursive, et cette variable recoit l'appel de la fonction find_min_rec(tab[:-1]). Donc le tableau moins le dernier élément
# => find_min_rec([32, 9]). A nouveau, lignes suivantes en attente de la valeur de find_min_rec(tab[:-1])

# RÉCURSION 2 - EXECUTION 3 => On rentre dans la 2 e poupée russe avec un tableau à 2 éléments
# la comparaison if len(tab) <= 1 renvoie false, on ne rentre donc pas dans ce if
# on passe dans le else => min_tab_temporaire recoit l'appel de la fonction récursive find_min_rec(tab[:-1])
# find_min_rec([32]). La suite du code de cette fonction est bloquée, on rentre dans la récursivité suivante
# RÉCURSION 3 - EXECUTION 4 => On rentre dans cette 3 e poupée russe

# Est ce que len(tab) <= 1, oui, le tableau ne fait qu'un seul élément. 1 <=1
# On retourne donc tab[0], qui est ici 32.


# RETOUR RÉCURSION 2 - EXCUTION 3 => Maintenant on sait que min_tab_temporaire vaut 32, on continue la suite du code
# Est ce que min_tab_temporaire < tab[-1] ? => Est ce que 32 < 9 ? => Cette condition renvoie false
# on bascule dans le else et on retourne tab[-1] => 9

# RETOUR RECURSION 1 - EXECUTION 2 => Maintenant min_tab_temporaire = 9 (retour de la fonction précédente).
# Est ce que 9 < 4 ? Non. Je rentre dans le else
# je retourne tab[-1] => ici 4

# RETOUR EXECUTION 1 => Maintenant min_tab_temporaire vaut 4
# 4 < 11 ? , oui, cette condition renvoie true
# on renvoie donc min_tab_temporaire qui vaut 4

# Réponse exacte : le minimum de tab_example : [32, 9, 4, 11] est bien 4.


# Exercice 10 : Code Wars : Tiling Rectangle with squares



# Exercice 11 : Retrouver le binaire d'un nombre

def dec_to_binary_rec(num):
    if num // 2 == 0:
        return str(num%2)
    else:
        return dec_to_binary_rec(num//2) + str(num%2)


print("test de dec à binaire", dec_to_binary_rec(8))

# il faut inverser et mettre dec_to_binary_rec(num//2), pour que la chaine de caractère se construise de droite à gauche
# 7%2 => 1
# 3%2 => 1
# 1%2 => 1
# Test avec 8
# 8%2 => 0
# 4%2 => 0
# 2%2 => 0
# 1%2 => 1
# return '0' + '0' + '0' + '1'
# return  '1' +'0' + '0' +'0'

#

# Exercice 12 : Vérifier qu’un tableau de nombre est trié par ordre croissant ou non

tab_sorted = [1,2,2,4,6]

tab_not_sorted = [12, 45, 59, 8, 600, 3, 21, 90, 32]

# Je vérifie que le tablea est trié par ordre croissant ou non
# ma condition d'arrêt, c'est que la taille du tableau est inférieure ou égale à 1.
# ce qu'il faut ensuite faire, c'est comparer les deux premiers éléments du tableau et retourner
# l'appel de la fonction récursive - le premier élément du tableau.
# Ou alors on le prend dans l'autre sens : il faut que l'avant dernier élément du tableau
# soit plus petit que le dernier élément du tableau, et retourner l'appel de la fonction récursive en lui
# passant en paramètres le tableau - le dernier élément

def is_sorted_rec(tab):
    if len(tab) <= 1:
        return True
    else:
        return tab[0] <= tab[1] and is_sorted_rec(tab[1:])


print("test du tableau", is_sorted_rec(tab_sorted))

print(tab_sorted[1:])



#
