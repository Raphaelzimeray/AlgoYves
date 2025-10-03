
from matplotlib import pyplot as plt
from time import time
# Exercice 1 : je fourni en paramètre deux années croisantes,
# et je veux que ca affiche les années qui vont de l’une à l’autre.
# Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.

def print_years_rec(year1, year2):
    if year1 > year2:
        pass
    else:
        print("voici l'année", year1)
        print_years_rec(year1 + 1, year2)

test_of_prints_years = print_years_rec(2010, 2025)
# print(test_of_prints_years)


# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n.

def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p-1)

test_of_power = power_rec(2,4)

print(test_of_power)

# Exercice 3 : Le nombre de chiffre d’un nombres. 1970 => 4
# // 10 (division entière)
# cdr (1970) = 1 + cdr(197)
# 1 + 1 + cdr(19)
# 1 + 1 + 1 + cdr(1)
# STOP condition d'arrêt

def count_digit_rec(n):
    if n < 9:
        return 1
    else:
        return 1 + count_digit_rec(n // 10)

print(count_digit_rec(1970))


# Exercice 4 : la somme des chiffres d’un nombre. 1972 = 1+9+7+2.
# première étape en partant de 1972 dans la fonction sod
# sod(1972) = 2 + sod(197)
# sod(1972) = 2 + 7 + sod(19)
# sod (1972) = 2 + 7 + 9 + sod (1)
# sod (1972) = 2 + 7 + 9 + 1


def sum_of_digits_rec(n):
    if n < 10:
        return n
    else:
        return n%10 + sum_of_digits_rec(n // 10)

print(sum_of_digits_rec(1972))


# suite de Fibonnaci

# pour n >= 2 ci dessous
# fib(n) = fib(n-1) + fib(n-2)

# fib(0) = 0
# fib(1) = 1
# fib(2) = fib(1) + fib(0)
# fib(2) = 1
# fib(3) = fib(2) + fib(1) => 2
# fib(4) = fib(3) + fib(2) => 2 + 1 => 3
# fib(5) = fib(4) + fib(3) => 3 + 2 => 5

def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# si je le fait avec 3
# fib_rec(3) = fib_rec(2) + fib_rec(1)
# fib_rec(3) = fib_rec(1) + fib_rec(0) + fib_rec()



for n in range(30, 40):
    print("fib (", n, ")=", fib_rec(n))


# comment améliorer le programme ? en mémorisant les résultats temporaires à l'aide d'une liste ou d'un dictionnaire (conteneur)

dico = {
    0: 0,
    1: 1,
    2: 1
}
# dico[3] = 2
# print(dico)


def fib_with_dico_rec(n):
    if n <= 1:
        return n
    else:
        if n - 1 not in dico:
            dico[n-1] = fib_with_dico_rec(n-1)
        if n - 2 not in dico:
            dico[n-2] = fib_with_dico_rec(n-2)
        return dico[n-1] + dico[n-2]

for n in range(30, 40):
    print("fibdico (", n, ")=", fib_with_dico_rec(n))

min = 2
max = 40

X = [x for x in range(min, max)]

fib__1 = []


for i in range (min, max):
    start = time()
    f = fib_rec(i)
    stop = time()
    fib__1.append(stop - start)

plt.plot(X,fib__1,label='fib rec')

fib__2 = []


for i in range (min, max):
    start = time()
    f = fib_with_dico_rec(i)
    stop = time()
    fib__2.append(stop - start)

plt.plot(X,fib__2,label='fib rec with dico')
plt.legend()
plt.show()
