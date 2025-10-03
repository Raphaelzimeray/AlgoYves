# Exercice : je fourni en paramètre deux années croisantes, et je veux que ca affiche les années qui vont de l’une à l’autre. Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.

def print_years_rec(year1, year2):
    if year1 >= year2:
        print("nous sommes à l'année", year1)
        return year1
    else:
        print("nous sommes à l'année", year1)
        return print_years_rec(year1 + 1, year2)


test_print_years_rec = print_years_rec(2003, 2025)

print(test_print_years_rec)


#ok

# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n.

def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p-1)


test_power_rec = power_rec(9, 9)

print(test_power_rec)

# Exercice 3 : Le nombre de chiffre d’un nombres. 1970 => 4


def number_of_digits_rec(n):
    if n <= 9:
        return 1
    else:
        return number_of_digits_rec(n // 10)


# test avec 1970
# => première étape = n

test_number_of_digits_rec = number_of_digits_rec(1979)

print(test_number_of_digits_rec)
