# Exercice1  : je fourni en paramètre deux années croisantes, et je veux que ca affiche les années qui vont de l’une à l’autre. Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.


def print_years_rec(year1, year2):
    if year2 < year1:
        print("c'est fini")
    else:
        print("Voici l'année", year1)
        return print_years_rec(year1 + 1, year2)


print(print_years_rec(2009, 2030))

#ok

# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n.

def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p -1)


test_power_rec = power_rec(2,9)
print(test_power_rec)

#ok


# Exercice 3 : Le nombre de chiffre d’un nombres. 32899 => 4
# si je divise en division entière // j'aurai un résultat entier
# premier tour de boucle, n > 10, je ne rentre pas dans le if
# => je rentre dans le else, j'augmente count de 1 et je retourne count digit rec(n//10)


def count_of_digits(n):
    if n < 1:
        return 0
    else:
        return 1 + count_of_digits(n//10)

# explications avec le chiffre 32899
# premier tour, 32899 > 1, je rentre dans le else => 1 + (count_of_digits(32899 // 10))
# deuxième tour, 3289 > 1, je rentre dans le else => 1 + (1 + count_of_digits(3289 // 10))
# troisième tour 328 > 1, je rentre dans le else => 1 + 1 + (1 + (count_of_digits(328 // 10))
# quatrième tour 32 > 1, je rentre dans le else => 1 + 1 + 1 + (1 + count_of_digits(32 //10))
# cinquème tour 3 > 1, je rentre dans le else => 1 + 1 + 1 + 1 + ( 1 + count_of_digits(3)) => 1 + 1 + 1 + 1 + 1 + 0 => 5


print(count_of_digits(32899))

# à refaire

# Exercice 4 : la somme des chiffres d’un nombre. 2033 = 2 + 0 + 3 + 3.

def sum_of_digits(n):
    if n < 1:
        return n
    else:
        return n%10 + sum_of_digits(n//10)

print(sum_of_digits(767))


# test avec 2033 => premier tour de boucle n est supérieur à 1, on passe dans le else, on a
# besoin d'avoir le 3 pour l'aditionner avec le reste.
# si je fais 2033 % 10 => je trouve 3. et ensuite, il faut que je divise le chiffre 2033 par 10 pour pouvoir recommencer cette
# opération lors de la fonction suivante donc n%10 + sum_of_digits(n//10) => 3 + sum_of_digits(203)
# => 2e tour => 3 + 3 + sum_of_digits(20)
# => 3e tour => 3 + 3 + 0 + sum_of_digits(2)
# => 4 e tour => 3 + 3 + 0 + 2 + sum_of_digits(0)
# => sortie => 3 + 3 + 0 + 2 + 0 => 8

print(2//10)



# Exercice 5 : Suite de fibonnaci


# Exercice 6 améliorer le programme en mémorisant les résultats temporaires à l'aide d'une liste ou d'un dictionnaire (conteneur)
