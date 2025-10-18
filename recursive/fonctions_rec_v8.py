from random import randint
from time import sleep

# Exercice 1 : je fourni en paramètre deux années croisantes, et je veux que ca affiche les années qui vont de l’une à l’autre.
# Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.

def print_years(year1, year2):
    if year1 > year2:
        print("")
    else:
        print(year1)
        return print_years(year1 + 1, year2)

print("test de la fonction print years", print_years(2014, 2019))

# ok

# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n.

def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p-1)


print("test de la fonction power rec", power_rec(2, 13))

# ok


# Exercice 3 : Le nombre de chiffre d’un nombres. 1970 => 4

def count_digits(n):
    if n //10 < 1:
        return 1
    else:
        return 1 + count_digits(n//10)

print("test de la fonction count digits", count_digits(239861))

# ok

# Exercice 4 : la somme des chiffres d’un nombre. 1970 = 1+9+7+0

def sum_of_digits(n):
    if n // 10 < 1:
        return n
    else:
        return n % 10 + sum_of_digits(n//10)

print("test de la fonction sum_of_ digits", sum_of_digits(2376))

# ok


# Exercice 5 : Afficher le chiffre de fibonacci

def print_fib_rec(n):
    if n <=1:
        return n
    else:
        return print_fib_rec(n-1) + print_fib_rec(n-2)

print("test de la fonction de fibonnaci", print_fib_rec(12))

# ok

# Exercice 6 : Fibonnaci : Optimiser le temps de calcul avec un dictionnaire temporaire

dico = {
    0: 0,
    1: 1
}

def print_fib_rec_with_dico(n):
    if n not in dico:
        dico[n] = print_fib_rec_with_dico(n-1) + print_fib_rec_with_dico(n-2)
    return dico[n]


print("test de la fonction fibonnaci optimisée", print_fib_rec_with_dico(12))


# Exercice 7 : Code Wars : Reduce My Fraction

def pgcd(a, b):
    if a == 1 or b == 1:
        return 1
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return pgcd(b%a, a)

def reduce_fraction(fraction):
    pgcd_num = pgcd(fraction[0], (fraction[1]))
    result = (fraction[0] // pgcd_num, fraction[1] // pgcd_num)
    return result



# Exercice 8 : Code Wars : Reduce My Fraction (version itérative)

# Exercice 9 : Vérifier si un mot est un palindrome

def is_palindrome_rec(word):
    if len(word) <=1:
        return word
    else:
        return word[0] == word[-1] and is_palindrome_rec(word[1:-1])

test_tab_palindrome = ["kayak", "eric", "jules", "non", "rever", "bonjour"]

for i in range (len(test_tab_palindrome)):
    if is_palindrome_rec(test_tab_palindrome[i]) == False:
        print(test_tab_palindrome[i], "n'est pas un palindrome")
    else:
        print(test_tab_palindrome[i], "est un palindrome")


# ok fonctionne, la fonction ne renvoie visiblement pas true si c'est un palindrome mais simplement false si c'est pas un palindrome


# Exercice 10 : Trouver le minimum d'un tableau

test_tab_min = [562, 123, 9009, 34, 4, 78, 30]

def find_min_rec(tab):
    if len(tab) <= 1:
        return tab[0]
    else:
        min_tab_temporaire = find_min_rec(tab[:-1])
        if min_tab_temporaire < tab[-1]:
            return min_tab_temporaire
        else:
            return tab[-1]

print("test du minimum du tableau", find_min_rec(test_tab_min))


# ok


# Exercice 11 : Retrouver le binaire d'un nombre

def find_binary_rec(n):
    if n // 2 == 0:
        return n%2
    else:
        return str(find_binary_rec(n//2)) + str(n%2)

print("test de la fonction dec to binary", find_binary_rec(586))

# décomposition avec 4 (on attend 100 en binaire)
# EXECUTION 1 - si n//2 == 0  =>  4//2 == 0  =>  2 == 0, cette condition renvoie false
# on passe dans le else. je divise le nombre à convertir par 2, et je note le reste de la division (1 ou 0)
# je retourne donc le str de la fonction récursive "find_binary_rec(n//2)"" =>  "find_binary_rec(4//2)" => "find_binary_rec(2)" + str(n%2)
# => "4%2" => 0. donc on retourne "find_binary_rec(2)" + "0"

# RÉCURSION 1 - EXECUTION 2 - si n//2 == 0 => 2//2 == 0 => 1 == 0, cette condition renvoie false
# on passe dans else. Je 

# Exercice 12 : Vérifier qu’un tableau de nombre est trié par ordre croissant ou non

# Exercice 13 : Vérifier qu'un nombre est premier

# Exercice 14 : Code Wars : Tiling Rectangles With squares

# Exercice 15 : Ecrire une fct récursive retournant la liste de toutes les permutations possibles d'une liste**

# Exercice 16 : Propagation (avec le fichier propagation.txt, remplir l'élément de "1" et de "2")

# Exercice 17 : Dichotomie
