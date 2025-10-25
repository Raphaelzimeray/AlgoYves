from random import randint
from time import sleep
import string, sys

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

print("test de pgcd version récursive", reduce_fraction((60,20)))


# décomposition avec 60 et 20
# EXECUTION 1  pgcd(a, b) -> pgcd(60, 20)
# on ne rentre pas dans les ifs
# on return pgcd(b%a, a) -> pgcd(20%60, 60) -> pgcd(20, 60)

# RÉCURSION 1 - EXECUTION 2 pgcd(20, 60)
# on ne rentre dans aucun des ifs
# on return pgcd(b%a, a) -> pgcd(60%20, 20) -> pgcd(0, 20)

# RÉCURSION 2 - EXECUTION 3
# on rentre dans if a == 0:
# on retourne b -> 20

# on ne remontera pas ici dans les différentes poupées russes parce qu'il ne reste plus de code "en attente d'être executé!"

# 60 // 20, 20 // 20
# 2, 1

# Exercice 8 : Code Wars : Reduce My Fraction (version itérative)

def pgcd_iterative(a, b):
    pass

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
# EXECUTION 1 - find_binary_rec(4) si n//2 == 0  =>  4//2 == 0  =>  2 == 0, cette condition renvoie false
# on passe dans le else. je divise le nombre à convertir par 2, et je note le reste de la division (1 ou 0)
# je retourne donc le str de la fonction récursive "find_binary_rec(n//2)"" =>  "find_binary_rec(4//2)" => "find_binary_rec(2)" + str(n%2)
# => "4%2" => 0. donc on retourne "find_binary_rec(2)" + "0"

# RÉCURSION 1 - EXECUTION 2 find_binary_rec(2) - si n//2 == 0 => 2//2 == 0 => 1 == 0, cette condition renvoie false
# on passe dans else.
# je retourne str de find_binary_rec(2//2) + str de n%2 (2%2)
# je retourne str de find_binary_rec(1) + str de 2%2(0)

# RÉCURSION 2 - EXECUTION 3 find_binary_rec(1)
# si n//2 == 0, => 1//2 == 0 , 0 == 0, cette condition renvoie true
# je retourne n%2 => 1%2 => 1.
# la poupée russe la plus petite vaut donc 1, la "moyenne" vaut 0 et la plus grande vaut 0, ce qui fait 100 concaténé.



# Exercice 12 : Vérifier qu’un tableau de nombre est trié par ordre croissant ou non

tab_not_sorted = [3, 8, 9, 1, 2, 40, 1]

tab_sorted = [1, 1, 2, 3, 8, 9, 40]

# version itérative

def check_sort(tab):
    for i in range(len(tab) -1):
        if tab[i] > tab[i+1]:
            return False
    return True


print("test de si tab_not_sorted est trié dans l'ordre croissant", check_sort(tab_not_sorted))
print("test de si tab_sorted est trié dans l'ordre croissant", check_sort(tab_sorted))


def check_sort_rec(tab):
    if len(tab) <= 1:
        print("le tableau est trié dans l'ordre croissant!")
        return True
    else:
        print(tab)
        return tab[0] <= tab[1] and check_sort_rec(tab[1:])

print("test de si tab_not_sorted est trié dans l'ordre croissant (recursive)", check_sort_rec(tab_not_sorted))
print("test de si tab_sorted est trié dans l'ordre croissant (recursive)", check_sort_rec(tab_sorted))



# Exercice 13 : Vérifier qu'un nombre est premier

# Version itérative

def isprime(n):
    for i in range(2, n-1):
        if n%i == 0:
            return False
    return True




for i in range(1,20):
    if isprime(i) == True:
        print(i, "est un nombre premier !")
    else:
        print(i, "est n'est pas un nombre premier!")

# Version récursive de l'emploi du %

def is_prime_rec(n, m):
    if m <= 1:
        return True
    return n%m != 0 and is_prime_rec(n,m-1)

def is_prime_2(n):
    return is_prime_rec(n,n//2)

# Décomposer avec 3
# EXECUTION 1 - is_prime_2(3)
# je retourne la fonction is_prime_rec(3, 1)

# EXECUTION 1 - is_prime_rec(3,1)
# if m <=1
# on rentre dans le if, on retourne True



# Décomposer avec 5
# EXECUTION 1 - is_prime_2(5)
# je retourne la fonction is_prime_rec(5, 2)

# EXECUTION 1 - is_prime_rec(5, 2)
# if m <=1
# if 2 <=1, cette condition renvoie false
# je return n%m != 0 and is_prime_rec(n,m-1)
# 5%2 != 0 and is_prime_rec(5,1)
# la premiere condition renvoie true, donc return true and is_prime_rec(5,1)

# EXEUCTION 2 - RÉCURSION 1 - is_prime_rec(5, 1)
# if m <=1
# if 1 <=1, cette condition renvoie true, je rentre dans le if
# je return True

# RETOUR EXECUTION 1 - is_prime_rec(5, 2)
# return true and true = true(le résultat de 5%2!=0 et le retour de l'execution 2 - récursion 1)

# RETOUR EXECUTION 1 - is_prime_2(5)
# je retourne le résultat de is_prime_rec(5,2) qui est true


for i in range(1,20):
    if is_prime_2(i) == True:
        print(i, "(rec)est un nombre premier !")
    else:
        print(i, "(rec)est n'est pas un nombre premier!")


# nombres premiers : 19, 31, 37, 53, 67
# nombres pas premiers : 14, 25, 42, 60, 75

# Exercice 14 : Code Wars : Tiling Rectangles With squares

# You have to cover a rectangular area (measuring n x m where n and m are positive integers) with square tiles.
# You have an unlimited supply of square tiles,
# but the lengths of the sides are all powers of 2 (1 x 1, 2 x 2, 4 x 4, 8 x 8, etc.).
# You must use the minimum number of tiles which will exactly cover the area.

# je regarde quel nombre puissance de 2 je peux mettre dans le plus petit coté du rectangle
# je défini d'abord quel est le plus coté du rectangle
# je fais ensuite une boucle while qui s'arrete quand le chiffre 2^n est > au plus petit coté
# à ce moment la, je retourne le chiffre n -1 car je suis allé une étape trop loin
# si le plus petit coté est = 11, je dois aller jusqu'à 2^4 = 16, je retire 1
# 2^3 = 8
# j'ai la taille du premier carré
# je dois ensuite déterminer la taille qu'il me reste dans les deux rectangles restants pour placer les autres carrés
# il reste deux zones à couvrir : la zone de droite et la zone du dessous
#


def num_tiles(width,height):
    if width <=1 or height <= 1:
        return width * height
    min_size = 0
    max_size = 0
    if width < height:
        min_size = width
        max_size = height
    else:
        min_size = height
        max_size = width
    print("test de min size", min_size)
    print("test de max size", max_size)
    power = 0
    while 2 ** power <= min_size:
        power = power + 1
        print("test de power", power)

    size_of_square = 2 ** (power -1)
    number_of_squares = max_size // size_of_square
    sum_square_size = number_of_squares * size_of_square
    return number_of_squares + num_tiles(min_size-size_of_square, sum_square_size) + num_tiles(min_size, max_size - sum_square_size)



print("test de num tiles", num_tiles(2, 2))


# Exercice 15 : Ecrire une fct récursive retournant la liste de toutes les permutations possibles d'une liste**

# Exercice 16 : Propagation (avec le fichier propagation.txt, remplir l'élément de "1" et de "2")

# on peut l'afficher en mode matrice en 2 dimensions, un certain nombre de lignes et un certain nombre de colonnes
# chaque lignes à le même nombre de caractères
# il y a un \n pour faire le retour à la ligne
# une matrice c'est une liste de liste, c'est une liste de dimension 2. Chaque élément du tableau est une liste.
# pour charger un fichier .txt !=json or csv
# utf-8 vs utf-16 (c'est le nombre d'octet dans lequel est codé un caractère) Unified text formating. En général utf-8

def search(getSol):
    pass

def propagation():
    pass


def getSol(file_name):
    sol = []
    with open(file_name, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            sol.append(list(ligne[:-1]))
    return sol

# execution du script
sol = getSol("data/propagation.txt")

for ligne in sol:
    print(ligne)

# on


# EXEMPLE AVEC un tableau de 2 dimensions
tab2d = [[0, 1, 2, 3], [4, 5, 6]]

# for l in tab2d:
#     print(l)

print("test de tab2d[1][1]: ",tab2d[1][1])
# print("test de len tab",len(tab2d))


for l in range(len(tab2d)):
    for c in range (len(tab2d[l])):
        print(tab2d[l][c], end= " ")
    print("")



# lignes = f.split('\n')
# tableau_2d = [ligne.split() for ligne in lignes]


# étape 1 : commencer à remplir le fichier avec des "1" partout
# itérer sur chaque lignes
# itérer sur chaque colonnes

# def fill_propagation_txt(tab):
#     print("je passe ici?")
#     for i in range(len(tab)):
#         print("je rentre dans le for i?")
#         print(tab[i])
#         for j in range(len(tab)):
#             print(tab[j])


# print("test de la taille du tableau", len(tableau_2d))

# print("test de la fonction fill propragation txt", fill_propagation_txt(tableau_2d))



# Exercice 17 : Dichotomie
