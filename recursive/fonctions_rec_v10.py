from random import randint
from matplotlib import pyplot as plt
from time import sleep

# Exercice 1 : je fourni en paramètre deux années croisantes, et je veux que ca affiche les années qui vont de l’une à l’autre.
# Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.


def print_years_rec(year1, year2):
    if year1 >= year2:
        print(year1)
    else:
        print(year1)
        return print_years_rec(year1 + 1, year2)


print_years_rec(2012, 2024)

#ok

# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n.

def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p-1)


print("test de power rec", power_rec(3, 4))

#ok

# Exercice 3 : Le nombre de chiffre d’un nombres. 1970 => 4


def number_of_digits_rec(n):
    if n //10 == 0:
        return 1
    else:
        return 1 + number_of_digits_rec(n //10)


print("Test de number of digits rec", number_of_digits_rec(23521))


# ok

# Exercice 4 : la somme des chiffres d’un nombre. 1970 = 1+9+7+0


def sum_of_digits_rec(n):
    if n // 10 == 0:
        return n%10
    else:
        return n%10 + sum_of_digits_rec(n//10)


print("Test de sum of digits rec", sum_of_digits_rec(1970))


# ok

# Exercice 5 : Afficher le chiffre de fibonacci


def fibo_rec(n):
    if n <= 1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

print("test de la fonction recursive fibonaci", fibo_rec(9))


# Exercice 6 : Fibonnaci : Optimiser le temps de calcul avec un dictionnaire temporaire

dico_fib = {
    0: 0,
    1: 1
}

def fibo_rec_with_dico(n):
    if n not in dico_fib:
        dico_fib[n] = fibo_rec_with_dico(n-1) + fibo_rec_with_dico(n-2)
    return dico_fib[n]


print("test de la fonction recursive fibonaci avec dictionnaire", fibo_rec_with_dico(9))



# Exercice 7 : Code Wars : Reduce My Fraction


def get_pgcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return get_pgcd(b%a, a)


def reduce_fraction(fraction):
    pgcd = get_pgcd(fraction[0], fraction[1])
    result = (fraction[0] // pgcd, fraction[1] // pgcd)
    return result



# Exercice 8 : Code Wars : Reduce My Fraction (version itérative)


# Exercice 9 : Vérifier si un mot est un palindrome

def is_palindrome_rec(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_rec(word[1:-1])


print("test de la fonction is palindrome", is_palindrome_rec("kayak"))


# Exercice 10 : Trouver le minimum d'un tableau

# comparer le minimum du tableau avec le minimum du tableau

def find_min_rec(tab):
    if len(tab) == 1:
        return tab[0]
    else:
        min_tab_temporaire = find_min_rec(tab[:-1])
        if min_tab_temporaire < tab[-1]:
            return min_tab_temporaire
        else:
            return tab[-1]


tab_test = [32, 12, 89, 11, 34]

print("test de find min rec", find_min_rec(tab_test))

# execution main du code avec un tableau test [32, 9, 5, 12]



# EXECUTION 1 => on rentre dans la fonction avec find_min_rec([32, 9, 5, 12])
# if len(tab) <= 1: => if 4 <= 1 => cette condition renvoie false, on passe au bloc else
# je déclare une variable min_tab_temporaire qui recoit l'appel de la fonction  find_min_rec(tab[:-1])
# donc min_tab_temporaire = find_min_rec([32, 9, 5])
# Je suis bloqué à cette étape d'execution puisque je n'ai aucune idée de la valeur de find_min_rec([32, 9, 5])
# Le code qui se trouve en dessous ne peut donc pas être executé, je dois rentrer dans la récursion

# RECURSION 1 - EXECUTION 2 => find_min_rec([32, 9, 5])
# if len(tab) <= 1: => if 3 <= 1: => cette condition renvoie false, on passe au bloc else
# min_tab_temporaire = find_min_rec(tab[:-1]) => min_tab_temporaire = find_min_rec([32, 9])
# impossible de poursuivre l'éxecution de cette fonction sans connaitre la valeur de find_min_rec([32, 9])
# je dois rentrer dans la recursion

# RECURSION 2 - EXECUTION 3 => find_min_rec([32, 9])
# if len(tab) <= 1: if 2 <= 1: => cette condition renvoie false, on passe au bloc else
# min_tab_temporaire = find_min_rec(tab[:-1]) => min_tab_temporaire = find_min_rec([32])
# impossible de poursuivre l'execution de cette fonction sans connaitre la valeur de find_min_rec([32])
# on passe dans la recursion

# RECURSION 3 - EXECUTION 4 => find_min_rec([32])
# if len(tab) <= 1: => if 1 <= 1: => cette condition renvoie true, on rentre dans le if
# on retourne tab[0] => ici 32.

# RETOUR RECURSION 2 - EXECUTION 3 => find_min_rec([32, 9])
# on connait maintenant la valeur de min_tab_temporaire (c'est 32)
# on va pouvoir passer à la suite du code
# if min_tab_temporaire < tab[-1] => if 32 < 9 => cette condition renvoie false
# on passe dans le else
# return tab[-1] => return 9

# RETOUR RECURSION 1 - EXECUTION 2 => find_min_rec([32, 9, 5])
# je reprend la ou je m'étais arreté, je sais que min_tab_temporaire (find_min_rec([32,9])) est égal à 9
# je poursuit l'execution du code
# if min_tab_temporaire < tab[-1]:
# if 9 < 5 => cette condition renvoie false, on passe dans le else
# return tab[-1] => 5

# RETOUR EXECUTION 1 => find_min_rec([32, 9, 5, 12])
# min_tab_temporaire = 5 (la valeur de find_min_rec([32, 9, 5]))
# if min_tab_temporaire < tab[-1]: => if 5 < 12, cette condition renvoie true
# je rentre dans le if je retourne min_tab_temporaire qui est égal à 5 et qui est bien le minimum du tableau















# Exercice 11 : Retrouver le binaire d'un nombre


def find_binary_rec(n):
    if n // 2 == 0:
        return str(n%2)
    else:
        return find_binary_rec(n//2) + str(n%2)


print("test de find binary rec", find_binary_rec(586))

# ok

# Exercice 12 : Vérifier qu’un tableau de nombre est trié par ordre croissant ou non (iteratif)

tab_sorted = [3, 5, 7, 9]
tab_sorted_2 = [2, 5, 7, 12]

tab_unsorted = [7, 8, 2, 9]
tab_unsorted_2 = [7, 12, 2, 9]


def is_sorted(tab):
    for i in range(len(tab) -1):
        if tab[i] > tab[i+1]:
            return False
    return True

print("vérifions si le tableau est trié dans l'ordre coissant", is_sorted(tab_sorted_2))
print("vérifions si le tableau est trié dans l'ordre coissant", is_sorted(tab_unsorted_2))



# Exercice 13 : Vérifier qu'un nombre est premier (itératif et récursif)

def is_prime(n):
    modulo = 2
    for i in range(modulo, n):
        if n % modulo == 0:
            return False
        modulo +=1
    return True

print("test de is prime", is_prime(80))

# si on test avec 4
# => 1 %2 !=0,
# => 2 %2 == 0

# Exercice 14 : Code Wars : Tiling Rectangles With squares



def num_tiles(width,height):
    if width == 0 or height == 0:
        return 0
    if width == 1 or height == 1:
        return width * height
    min_size = 0
    max_size = 0
    if width < height:
        min_size = width
        max_size = height
    else:
        min_size = height
        max_size = width
    power = 0
    while 2 ** power <= min_size:
        power +=1
    size_of_square = 2 ** (power-1)
    number_of_squares = max_size // size_of_square
    print(number_of_squares)
    return number_of_squares + num_tiles(max_size - (size_of_square * number_of_squares), size_of_square) + num_tiles(min_size - size_of_square, max_size)


print("number of squares", num_tiles(13, 11))

# Exercice 15 : Ecrire une fct récursive retournant la liste de toutes les permutations possibles d'une liste**


# Exercice 16 : Propagation (avec le fichier propagation.txt, remplir l'élément de "1" et de "2")


# Exercice 17 : Dichotomie
