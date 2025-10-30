from random import randint
from matplotlib import pyplot as plt
from time import sleep

# Exercice 1 : je fourni en paramètre deux années croisantes, et je veux que ca affiche les années qui vont de l’une à l’autre.
# Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.

def print_years_rec(year_1, year_2):
    if year_1 > year_2:
        print("Terminé")
    else:
        print(year_1)
        return print_years_rec(year_1 + 1, year_2)


print("test de print years rec", print_years_rec(1978, 2025))

# ok

# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n.

def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p -1)


print("test de power rec", power_rec(2,5))

# ok

# Décomposition avec 2^5

# EXECUTION 1 : power_rec(2,5)
# p == 1 => 5 == 1, cette condition renvoie false, je passe dans le else
# je retourne n * power_rec(n, p -1) => 2 * power_rec(2, 4)

# RÉCURSION 1 - EXECUTION 2 : power_rec(2, 4)
# p == 1 => 4 == 1, cette condition renvoie false, je passe dans le else
# je retourne n * power_rec(n, p -1) => 2 * power_rec(2, 3)

# RÉCURSION 2 - EXECUTION 3 : power_rec(2, 3)
# p == 1 => 3 == 1, cette condition renvoie false, je passe dans le else
# je retourne n * power_rec(n, p-1) => 2 * power_rec(2, 2)

# RÉCURSION 3 - EXECUTION 4 : power_rec(2, 2)
# p == 1 => 2 == 2, cette condition renvoie false, je passe dans le else
# je retourne n * power_rec(n, p-1) => 2 * power_rec(2, 1)

# RÉCURSION 4 - EXECUTION 5 : power_rec(2, 1)
# p == 1 => 1 == 1, cette condition renvoie true, je retourne n (2)

# RETOUR RÉCURSION 3 - EXECUTION 4 : power_rec(2, 2)
# je suis fixé sur la valeur de power_rec(2, 1), c'est 2.
# donc 2 * 2 = 4

# RETOUR RÉCURSION 2 - EXECUTION 3 : power_rec(2, 3)
# je suis fixé sur la valeur de power_rec(2, 2), c'est 4
# donc 2 * 4 = 8

# RETOUR RÉCURSION 1 - EXECUTION 2 : power_rec(2, 4)
# je suis fixé sur la valeur de power_rec(2, 3), c'est 8
# donc 2 * 8 = 16

# RETOUR EXECUTION 1 : power_rec(2, 5)
# je suis fixé sur la valeur de power_rec(2, 4), c'est 16
# donc 2 * 16 = 32




# Exercice 3 : Le nombre de chiffre d’un nombres. 1970 => 4


def count_of_digits_rec(n):
    if n <= 10:
        return 1
    else:
        return 1 + count_of_digits_rec(n // 10)


print("test de count of digits rec", count_of_digits_rec(67329))

# ok

# Décomposition avec 67329
# EXECUTION 1 : sum_of_digits_rec(67329)
# n <= 10 => 67329 <=10, cette condition renvoie false
# on passe dans le else
# je return 1 + sum_of_digits_rec(n // 10) => 1 + sum_of_digits_rec(6732)

# RÉCURSION 1 - EXECUTION 2 : sum_of_digits_rec(6732)
# n <= 10 => 6732 <= 10, cette condition renvoie false
# on passe dans le else
# je return 1 + sum_of_digits_rec(n // 10) => 1 + sum_of_digits_rec(673)

# RÉCURSION 2 - EXECUTION 3 : sum_of_digits_rec(673)
# n <= 10 => 673 <= 10, cette condition renvoie false
# on passe dans le else
# je return 1 + sum_of_digits_rec(n // 10) => 1 + sum_of_digits_rec(67)

# RÉCURSION 3 - EXECUTION 4 : sum_of_digits_rec(67)
# n <= 10 => 67 <= 10, cette condition renvoie false
# on passe dans le else
# je return 1 + sum_of_digits_rec(n // 10) => 1 + sum_of_digits_rec(6)

# RÉCURSION 4 - EXECUTION 5 : sum_of_digits_rec(6)
# n <= 10 => 6 <= 10, cette condition renvoie true,
# on return 1

# RETOUR RÉCURSION 3 - EXECUTION 4 : sum_of_digits_rec(67)
# je suis fixé sur la valeur de sum_of_digits_rec(6), qui est 1
# donc 1 + 1 = 2

# RETOUR RÉCURSION 2 - EXECUTION 3 : sum_of_digits_rec(673)
# je suis fixé sur la valeur de sum_of_digits_rec(67), qui est 2
# 1 + 2 = 3

# RETOUR RÉCURSION 1 - EXECUTION 2 : sum_of_digits_rec(6732)
# je suis fixé sur la valeur de sum_of_digits_rec(673), qui est 3
# 1 + 3 = 4

# RETOUR EXECUTION 1 : sum_of_digits_rec(67329)
# je suis fixé sur la valeur de sum_of_digits_rec(6732), qui est 4
# 1 + 4 = 5





# Exercice 4 : la somme des chiffres d’un nombre. 1970 = 1+9+7+0


def sum_of_digits_rec(n):
    if n <=10:
        return n % 10
    else:
        return n % 10 + sum_of_digits_rec(n//10)


print("Test de sum of digits rec", sum_of_digits_rec(3243))

# ok


# Exercice 5 : Afficher le chiffre de fibonacci

def print_fib_rec(n):
    if n <= 1:
        return n
    else:
        return print_fib_rec(n-1) + print_fib_rec(n-2)


print("Test de print fib rec", print_fib_rec(12))

# ok

# à décomposer avec 8


# Exercice 6 : Fibonnaci : Optimiser le temps de calcul avec un dictionnaire temporaire

dico_fib = {
    0: 0,
    1: 1
}

def print_fib_rec_with_dico(n):
    if n not in dico_fib:
        dico_fib[n] = print_fib_rec_with_dico(n-1) + print_fib_rec_with_dico(n-2)
    return dico_fib[n]



print("Test de print fib rec with dico", print_fib_rec_with_dico(12))



# Exercice 7 : Code Wars : Reduce My Fraction

def get_pgcd(a, b):
    if a == 1 or b == 1:
        return 1
    if a == 0:
        return b
    if b == 0:
        return a
    return get_pgcd(b%a, a)




def reduce_fraction(fraction):
    pgcd_result = get_pgcd(fraction[0], fraction[1])
    result = (fraction[0] // pgcd_result, fraction[1] // pgcd_result)
    return result



print("Test de reduce fraction en itérative", reduce_fraction((60, 20)))


# Exercice 8 : Code Wars : Reduce My Fraction (version itérative)

def reduce_fraction_iterative(fraction):
    diviseurs_fraction_0 = []
    diviseurs_fraction_1 = []
    for i in range(1, fraction[0] + 1):
        if fraction[0] % i == 0:
            diviseurs_fraction_0.append(i)
    for i in range(1, fraction[1] + 1):
        if fraction[1] % i == 0:
            diviseurs_fraction_1.append(i)
    max_in_both = max(filter(lambda x: x in diviseurs_fraction_0, diviseurs_fraction_1))
    return (fraction[0] // max_in_both, fraction[1] // max_in_both)


print("Test de reduce fraction en iterative", reduce_fraction_iterative((60,20)))


# Exercice 9 : Vérifier si un mot est un palindrome


list_word = ["kayak", "rotor", "bonjour", "radar", "rever", "manger"]

def is_palindrome_rec(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_rec(word[1:-1])



for i in range(len(list_word)):
    if is_palindrome_rec(list_word[i]) == True:
        print("le mot", list_word[i], "est un palindrome !")
    else:
        print("le mot", list_word[i], "n'est pas un palindrome !")




# Exercice 10 : Trouver le minimum d'un tableau


tab_test= [randint(1,100) for i in range(20)]
print(tab_test)
tab_demo = [8, 5, 9, 4]


def find_min_rec(tab):
    if len(tab) <= 1:
        return tab[0]
    else:
        min_tab_temporaire = find_min_rec(tab[:-1])
        if min_tab_temporaire < tab[-1]:
            return min_tab_temporaire
        else:
            return tab[-1]


print("Test de find min rec", find_min_rec(tab_test))

print("Test de find min rec avec le tableau de demo", find_min_rec(tab_demo))


# Décomposition avec un tableau à 4 éléments tab_demo = [8, 5, 9, 4]

# EXECUTION 1 : je rentre dans find_min_rec(tab_demo) => find_min_rec([8, 5, 9, 4])
# est ce que len(tab) <=1 => 4 <= 1, cette condition renvoie false,
# je passe dans le else
# je déclare une varibale min_tab_temporaire = find_min_rec(tab[:-1]) => min_tab_temporaire = find_min_rec([8, 5, 9])
# donc min_tab_temporaire recoit l'appel de la fonction récursive avec le tableau amputé d'un élément

# RÉCURSION 1 - EXECUTION 2 : je rentre dans find_min_rec([8, 5, 9])
# est ce que len(tab) <= 1 => 3 <= 1, cette condition renvoie false,
# je passe dans le else
# je déclare une variable min_tab_temporaire = find_min_rec(tab[:-1]) => min_tab_temporaire = find_min_rec([8,5])

# RÉCURSION 2 - EXECUTION 3 : je rentre dans find_min_rec([8,5])
# est ce que len(tab) <=1 => 2 <= 1, cette condition renvoie false,
# je passe dans le else
# je déclare une variable min_tab_temporaire = find_min_rec(tab[:-1]) => min_tab_temporaire = find_min_rec([8])

# RÉCURSION 3 - EXECUTION 4 : je rentre dans find_min_rec([8])
# est ce que len(tab) <=1 => 1 <= 1, cette condition renvoie TRUE,
# je rentre dans le if, et je return tab[0] => 8


# RETOUR RÉCURSION 2 - EXECUTION 3 :
# je suis fixé sur la valeur de min_tab_temporaire qui est égale à 8
# je peux continuer à executer le reste du code.
# if min_tab_temporaire < tab[-1]: => if 8 < 5
# cette condition renvoie false, je passe dans le else
# je return tab[-1] => 5

# RETOUR RÉCURSION 1 - EXECUTION 2 :
# je suis fixé sur la valeur de min_tab_temporaire = 5
# je peux continuer à executer le reste du code.
# if min_tab_temporaire < tab[-1]: => if 5 < 9
# cette condition renvoie true, je return min_tab_temporaire = 5

# RETOUR EXECUTION 1 :
# Je suis fixé sur la valeur de min_tab_temporaire = 5
# je peux continuer à executer le reste du code.
# if min_tab_temporaire < tab[-1]: => if 5 < 4
# cette condition renvoie false, je passe dans le else
# je return tab[-1] => 4

# le minimum du tableau est bien 4 !






# Exercice 11 : Retrouver le binaire d'un nombre


def find_binary_rec(num):
    if num // 2 == 0:
        return str(num%2)
    else:
        return find_binary_rec(num//2) + str(num%2)


print("Test de find binary rec", find_binary_rec(40))


# ok

# décomposer le code pour comprendre l'importance de l'ordre str(num%2) après le return



# Exercice 12 : Vérifier qu’un tableau de nombre est trié par ordre croissant ou non (itérative)

tab_sorted = [3, 6, 9, 12, 15]

tab_unsorted = [1, 2, 8, 9, 1, 30, 11]


def is_sorted(tab):
    for i in range(len(tab) -1):
        if tab[i] > tab[i+1]:
            return False
    return True

print("Test de is sorted avec tableau trié : ", is_sorted(tab_sorted))

print("Test de is sorted avec tableau trié: ", is_sorted(tab_unsorted))




# Exercice 13 : Vérifier qu'un nombre est premier (itératif et récursif)

nombres = [14, 19, 25, 31, 37, 42, 53, 60, 67, 75]


def is_prime_iteratif(n):
    modulo = 2
    for i in range(modulo, n):
        if n%modulo == 0:
            return False
        modulo +=1
    return True



for i in range(len(nombres)):
    if is_prime_iteratif(nombres[i]) == True:
        print(nombres[i], "est un nombre premier")
    else:
        print(nombres[i], "n'est pas un nombre premier !")




# nombres premiers : 19, 31, 37, 53, 67
# nombres pas premiers : 14, 25, 42, 60, 75



# Exercice 14 : Code Wars : Tiling Rectangles With squares

# sur 11, 18 => trouver le plus grand carré qu'on peut placer et combien on peut en mettre
# pour savoir combien on peut en mettre on prend le plus petit coté du rectangle
# on cherche quel est la plus grande puissance de 2 qui soit inférieure au plus petit côté du rectangle
# on fait une boucle while, des qu'on dépasse 2^n > min_size => on stoppe, et on devra stocker le 2^n-1 dans la variable car on est allés
# un cran trop haut par rapport au coté le plus petit
# ensuite pour savoir combien de carrés on pourra placer dans le rectangle, il faudra calculer le nombre de carrés qu'on peut disposer
# dans la longeur la plus longue du rectangle
# ensuite j'appelle deux fonctions récursives avec les parties qui nous restent à couvrir, à savoir
# le coté droit du rectangle qu'il reste à couvrir,
# le bas du rectangle qu'il reste à couvrir.


def num_tiles(width,height):
    if width == 0 or height == 0:
        return 0
    if width == 1 or height == 1:
        return width * height
    min_length = 0
    max_length = 0
    if width < height:
        min_length = width
        max_length = height
    else:
        min_length = height
        max_length = width
    power = 0
    while 2** power <= min_length:
        power +=1
    size_square = 2 ** (power -1)
    number_of_squares = max_length // size_square

    return number_of_squares + num_tiles(size_square, max_length - (size_square * number_of_squares)) + num_tiles( min_length - size_square, max_length)



print("test num tiles", num_tiles(11, 13))


# décomposition du code avec 11, 13

# EXECUTION 1 : num_tiles(11, 13)
# je ne rentre dans aucun des ifs
# min_length = 0, max_length = 0
# if width < height: => if 11 < 13, cette condition renvoie true, je rentre dans le if
# min_length = width max_length = height => min_length = 11, max_length = 13
# power = 0
# BOUCLE WHILE TOUR 1
# while 2** power <= min_length: => while 2 ** 0 <= min_length => while 1 <= 11, cette condition renvoie true, je rentre dans le while
# power +=1, 0 += 1 => power = 1
# BOUCLE WHILE TOUR 2
# while  2** power <= min_length: => while 2 ** 1 <= min_length => while 2 <= 11, cette condition renvoie true, je rentre dans le while
# power +=1, 1+=1 => power = 2
# BOUCLE WHILE TOUR 3
# while  2** power <= min_length: => while 2 ** 2 <= min_length => while 4 <= 11, cette conditon renvoie true, je rentre dans le while
# power +=1, 2+=1, power = 3
# BOUCLE WHILE TOUR 4
# while 2** power <= min_length: => while 2 ** 3 <= min_length => while 8 <= 11, cette condition renvoie true, je rentre dans le while
# power +=1 => 3+=1, power = 4
# BOUCLE WHILE TOUR 5
# while 2** power <=  min_length:  => while 2 ** 4 <= min_length => while 16 <= 11, cette condition renvoie false, je ne rentre donc pas dans le while
# power = 4, il faut retirer 1 car on est allé une étape trop haute
# size_square = 2 ** (power -1) => size_square = 2 ** (4-1) => 2 ** 3 => 8
# la taille du carré est 8
# number_of_squares = max_length // size_square
# number_of_squares = 13 // 8 => 1
# return number_of_squares + num_tiles(size_square, max_length - (size_square * number_of_squares)) + num_tiles( min_length - size_square, max_length)
# return 1 + num_tiles(8, 13 - (8 * 1)) + num_tiles(11 - 8, 13)
# return 1 + num_tiles(8, 5) + num_tiles(3, 13)

# RECURSION 1.1 : EXECUTION 2.1 num_tiles(8, 5)
# je ne rentre dans aucun des ifs
# min_length = 0, max_length = 0
# if width < height: => if 8 < 5, cette condition renvoie false, je rentre dans le else
# min_length = height, max_length = width
# min_length = 5, max_length = 8
# power = 0¨
# BOUCLE WHILE TOUR 1
# while 2** power <= min_length:
# while 2 ** 0 <= 5
# while 1 <= 5, cette condition renvoie true, on rentre dans le while
# power +=1
# 0+=1
# power = 1
# BOUCLE WHILE TOUR 2
# while 2** power <= min_length:
# while 2 ** 1 <= 5
# while 2 <= 5, cette condition renvoie true, on rentre dans le while
# power += 1
# 1+=1
# power = 2
# BOUCLE WHILE TOUR 3
# while 2** power <= min_length:
# while 2 ** 2 <= 5
# while 4 <= 5, cette condition renvoie true, on rentre dans le while
# power += 1
# 2+=1
# power = 3
# BOUCLE WHILE TOUR 4
# while 2** power <= min_length:
# while 2 ** 3 <= 5
# while 8 <= 5, cette condition renvoie false, on sort du while
# power = 3
# size_square = 2 ** (power -1)
# size_square = 2 ** (3 -1)
# size_square = 2 ** 2
# size_square = 4
# number_of_squares = max_length // size_square
# number_of_squares = 8 // 4
# number_of_squares = 2
# return number_of_squares + num_tiles(size_square, max_length - (size_square * number_of_squares)) + num_tiles( min_length - size_square, max_length)
# return 2 + num_tiles(4, 0) + num_tiles(1, 8)



# RECURSION 1.1.1 - EXECUTION 2.1.1 num_tiles(4, 0)
# if height <= 1:
# if 0 <= 1, cette condition renvoie true, on rentre dans le if
# on retourne width qui est égal à 4
# on retourne 4.

# RECURSION 1.1.2 - EXECUTION 2.1.2 num_tiles(1, 8)¨
# if width <= 1
# if 1 <= 1, cette condition renvoie true, on rentre dans le if
# on retourne height qui est égale à 8
# on retourne 8






# RECURSION 1.2 - EXECUTION 2.2 num_tiles(3, 13)
# je ne rentre dans aucun des ifs
# min_length = 0 max_length = 0
# if width < height:
# if 3 < 13, cette condition renvoie true, je rentre dans le if
# min_length = width max_length = height
# min_length = 3, max_length = 13
# power = 0
# BOUCLE WHILE TOUR 1
# while 2** power <= min_length:
# while 2 ** 0 <= 3
# while 1 <= 3, cette condition renvoie true
# je rentre dans le while
# power += 1
# 0+=1
# power = 1
# BOUCLE WHILE TOUR 2
# while 2** power <= min_length:
# while 2 ** 1 <= 3
# while 2 <= 3,cette condition renvoie true, je rentre dans le while
# power +=1
# 1+=1 => power = 2
# BOUCLE WHILE TOUR 3
# while 2** power <= min_length:
# 2 ** 2 <= 3
# 4 <=3, cette condition renvoie false, je ne rentre pas dans le while
# power = 2
# size_square = 2 ** (power -1)
# size_square = 2 ** 1
# size_square = 2
# number_of_squares = max_length // size_square
# number_of_squares = 13 // 2
# number_of_squares = 6
# return number_of_squares + num_tiles(size_square, max_length - (size_square * number_of_squares)) + num_tiles(min_length - size_square, max_length)
# return 6 + num_tiles(2, 1) + num_tiles(1, 13)

# RECURSION 1.2.1 - EXECUTION 2.2.1 num_tiles(2, 1)
# if height <= 1:
# if 1 <= 1, cette condition renvoie true
# je retourne width qui est égale à 2
# je retourne 2

# RECURSION 1.2.2 - EXECUTION 2.2.2 num_tiles(1, 13)
# if width <= 1:
# if 1 <= 1:
# je retourne height qui est égale à 13
# je retourne 13


# RETOUR RECURSION 1.2 - EXECUTION 2.2 num_tiles(3, 13)
# Je suis fixé sur num_tiles(2, 1) (2) et num_tiles(1, 13) (13)
# Le retour de la fonction est donc 6 + 2 + 13 => 21

# RETOUR RECURSION 1.1 - EXECUTION 2.1 num_tiles(8, 5)
# Je suis fixé sur num_tiles(4, 0) (4) et sur num_tiles(1, 8) (8)
# Le retour de la fonction est donc 2 + 4 + 8 => 12

# RETOUR EXECUTION 1
# Je suis fixé sur num_tiles(3, 13) (21) et  num_tiles(8, 5) (12)
# je retourne donc 1 + 21 + 12 => 34







# Exercice 15 : Ecrire une fct récursive retournant la liste de toutes les permutations possibles d'une liste**


# Exercice 16 : Propagation (avec le fichier propagation.txt, remplir l'élément de "1", de "2" et de "3")

# importing os module



# gives the path of demo.py
def getSol(file_name):
    sol = []
    with open(file_name, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            sol.append(list(ligne[:-1]))
    return sol

sol = getSol('data/propagation.txt')

print(sol)



def propagation(file):
    value = 1
    for l in range(len(file)):
        for c in range(len(file[l])):
            if file[l][c] == "X":
                file[l][c] = "-"
            if file[l][c] == " ":
                fill_tab(file, value, l, c)
                value +=1
    return file


def fill_tab(file, value, l, c):
    if l >= 0 and l < len(file) -1 and c >=1 and c < len(file[l]) -1 and file[l][c] == " ":
        file[l][c] = value
        fill_tab(file, value, l +1, c)
        fill_tab(file, value, l -1, c)
        fill_tab(file, value, l, c+1)
        fill_tab(file, value, l, c-1)



# file_with_propagation = propagation(sol)

# print(file_with_propagation)


# for l in range(len(file_with_propagation)):
#     for c in range(len(file_with_propagation[l])):
#         print(file_with_propagation[l][c], end=" ")
#     print("")


sol_2 = propagation(sol)

for l in sol_2:
    for c in l:
       print(c, end=" ")
    print("")


# print("Test du fichier avec les 1", propagation(sol))



# Exercice 17 : Dichotomie
