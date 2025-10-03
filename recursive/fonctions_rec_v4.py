# Exercice 1: je fourni en paramètre deux années croisantes, et je veux que ca affiche les années qui vont de l’une à l’autre.
# Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.
from random import randint
from time import sleep

def print_years_rec(year1, year2):
    if(year2 < year1):
        print("terminé !")
    else:
        print(year1)
        return print_years_rec(year1 + 1, year2)

print_years_rec(2010, 2013)

# explication avec 2010 en year1 et 2013 en year2
# premier tour => on check si 2013 < 2010 => ligne 6, ca retourne false, on passe dans le else
# j'affiche l'année year 1 => ici 2010
# je retourne l'appel de la première récursivité print_years_rec(year1 + 1, year2) => print_years(2011, 2013)
# première récursivité, deuxième execution de la fonction => on check si 2013 < 2011, ligne 6, ca retourne false, on passe dans le else
# j'affiche l'année year 1 => ici 2011
# je retourne l'appel de la deuxième récursivité print_years_rec(year1 + 1, year2) => print_years(2012, 2013)
# deuxième récursivité, troisième execution de la fonction => on check si 2012 < 2013, ligne 6, ca retourne false
# on passe dans le else
# j'affiche l'année year1 => ici 2012
# je retourne l'appel de la troisième récursivité print_years_rec(year1 + 1, year2) => print_years(2013, 2013)
# troisième récursivité, 4e execution de la fonction => on check si 2013 < 2013, ligne 6, ca retourne false, on passe dans le else
# j'affiche l'année year1 => ici 2013
# je retourne l'appel de la quatrième récursivité print_years_rec(year1 + 1, year2) => print_years(2014, 2013)
# 4 e récursivité, 5 e appel de la fonction => on check si 2014 < 2013, ligne 6, ca retourne true, on print("terminé")



# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n. Le


def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p-1)


print(power_rec(3,10))


# Exercice 3 : Le nombre de chiffre d’un nombres.

def count_digits(n):
    if n < 1:
        return 0
    else:
        return 1 + count_digits(n//10)

print(count_digits(198438))


# Exercice 4 : la somme des chiffres d’un nombre. ex 4437 => doit retourner 18

def sum_of_digits(n):
    if n <= 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

print(sum_of_digits(4438))
# j'ai besoin du résultat du %10 => 7 au premier tour, et ensuite de couper le chiffre en lui retirant 1 division entière par 10 (//10)
# donc je dois additionner le %10 de n et ajouter l'appel de la fonction récursive sum_of_digits(n//10) => n%10 + sum_of_digits(n//10)
# donc 7 + sum_of_digits(n//10)
# première récursion => 443 % 10 => 3 + sum_of_digits(n//10) => 7 + (3 + sum_of_digits(44))
# deuxième récursion => 44 %10 => 4 + sum_of_digits(n//10) => 7 + 3 + (4 + sum_of_digits(4))
# troisième récursion => 4 %10 => 4 + sum_of_digits(n//10) => 7 + 3 + 4 + 4 + sum_of_digits(0)
# dernière récursion, on rentre dans le if, on retourne 0.
# total des opérations sur les fonctions récursives cumulées => 10 + 18 => 18 fonctionne


# Exercice 5 : CodeWars, reduce my fraction
# 60/20 => 3/1
# 80/120 => 2/3
# 45 / 120 => 3/8

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
    return (fraction[0]/ result, fraction[1]/ result)


# Décomposition des étapes avec 45 / 120
# On entre dans la fonction get_pgcd avec les deux paramètres 45 et 120. get_pgcd(45, 120)
# on ne rentre pas dans les 3 premiers if (ils retournent tous false), on bascule dans le return de la fonction
# récursive get_pgcd(b%a, a) => donc get_pgcd(120%45, 45) => get_pgcd(30, 45)
# Première récursivité, 2 e fois que la fonction s'éxecute => on ne rentre pas dans les 3 premiers if (ils retournent tous false), on bascule dans le return de la fonction
# recursive get_pgcd(b%a, a) => donc get_pgcd(45%30, 30) => get_pgcd(15, 30)
# Deuxième récursivité, 3 e fois que la fonction s'éxecute => on ne rentre pas dans les 3 premiers if (ils retournent tous false), on bascule dans le return de la fonction
# recursive get_pgcd(b%a, a) => donc get_pgcd(30%15, 15) => get_pgcd(0, 15)
# Troisième récursivité, 4 e fois que la fonction s'execute => a = 0, on rentre dans ce if et on retourne b. => Je retourne 15
# ma fonction reduce_fraction va donc se servir de mon 15 pour effectuer la division sur chaque élément de la fraction et voir le résultat
# 45/15, 120/15 => 3 / 8


# Exercice 6 => Suite de Fibonnaci
# afficher la suite de fibonnaci entre deux nombres

def print_fibonaci_rec(a):
    if a <= 1:
        return a
    return print_fibonaci_rec(a-1) + print_fibonaci_rec(a-2)



# Décomposition du code
# Explication professeur
# Dans Fibonacci en récursif comme dans toute fct récursive, la valeur du paramètre va descendre depuis la valeur initiale,
#  par exemple calculer print_fibonaci_rec(12), puis appeler en poupée russe print_fibonaci_rec(11)+ print_fibonaci_rec(10),
#  etc, jusqu'à print_fibonaci_rec(1) et print_fibonaci_rec(0). Or ces 2 valeurs sont connues : print_fibonaci_rec(1) = 1 et print_fibonaci_rec(0) = 0.
# Le test d’arrêt consiste donc à tester si le paramètre d'entrée vaut 0 ou 1 et dans ce cas de retourner la valeur déjà connue.

# Test
# Sur print_fibonaci_rec(3)
# je rentre dans la fonction, 3 != 1 et 3!= 0, je ne rentre pas dans ces ifs, je passe au return de la fonction récursive
# première poupée russe fib(2) + fib(1) ce qui équivaut à dire print_fibonaci_rec(3-1) + print_fibonaci_rec(3-2)
# donc print_fibonaci_rec(a-1) + print_fibonaci_rec(a-2)
# Je réalise donc que j'ai deux fonctions récursives qui découlent de la première execution de la fonction
# (print_fibonaci_rec(3)) : print_fibonaci_rec(a-1) + print_fibonaci_rec(a-2)
# on a donc deux fonctions à traiter : print_fibonaci_rec(a-1) + print_fibonaci_rec(a-2)
# première fonction (récursion 1.1) =>  print_fibonaci_rec(a-1) => print_fibonaci_rec(2) => on ne rentre pas dans les ifs
# on retourne print_fibonaci_rec(a-1) + print_fibonaci_rec(a-2) => print_fibonaci_rec(1) + print_fibonaci_rec(0)
# on a deux fonctions à traiter : print_fibonaci_rec(1) (retournera 1) et print_fibonaci_rec(0) (retournera 0)
# donc on a 1 + la deuxième fonction de la récursion (récursion 1.2) => print_fibonaci_rec(a-2) => print_fibonaci_rec(3-2) => print_fibonaci_rec(1) => 1
# donc 1 + 1 => 2

print("test de fib sans le dico v1",print_fibonaci_rec(11))




# Exercice 7 : Faire la même chose avec un dicionnaire temporaire pour éviter d'épuiser le processeur de l'ordinateur

# Explications du professeur
# A départ, ton dictionnaire a 2 entrées connues : fib[0] = 0 et fib[1] = 1. les autres entrées vont s'ajouter au fur et à mesure du besoin du calcul
#
# dans notre cas si on a fib_rec_with_dico(3)
# je rentre dans la fonction TRONC PRINCIPAL => je vérifie si la réponse est déja dans le dictionnaire
# la réponse n'est pas dans le dictionnaire, je vérifie si 3 est <= 1. Ce n'est pas le cas, donc je continue
# je passe dans le return  fib_rec_with_dico(a-1) + fib_rec_with_dico(a-2)
# Je réalise donc que j'ai deux fonctions récursives qui découlent de la première execution de la fonction
# cela va créer deux branches, BRANCHE 1, BRANCHE 2
# (fib_rec_with_dico(3)) : fib_rec_with_dico(a-1) + fib_rec_with_dico(a-2)
# on a donc deux fonctions à traiter : fib_rec_with_dico(a-1) + fib_rec_with_dico(a-2)
# première fonction BRANCHE 1, première branche de l'arbre (récursion 1.1) => fib_rec_with_dico(a-1) => fib_rec_with_dico(2) => on ne rentre pas dans le if a <= 1:
# on retourne donc fib_rec_with_dico(a-1) + fib_rec_with_dico(a-2) => fib_rec_with_dico(2) +fib_rec_with_dico(1)
# => fib_rec_with_dico(2) + 1
# BRANCHE 1.1 + 1
# => deux nouvelles branches fib_rec_with_dico(a-1) + fib_rec_with_dico(a-2) => fib_rec_with_dico(1)(BRANCHE 1.1.1) + fib_rec_with_dico(0) (BRANCHE 1.1.2) => 1
# Maintenant, quand je remonte des feuilles jusqu'au tronc, je vais pouvoir remplir le dictionnaire au fur et à mesure parce que j'en sais
# plus sur les valeurs de fib à tel et tel index
# BRANCHE 1.1 => fib_rec_with_dico(2) => cette valeur n'est pas renseignée dans le dictionnaire, donc je vais push dans le tableau
# sa valeur.
# Si je remonte à la branche numéro 1 BRANCHE 1 => Je connait maintenant la valeur de fib_rec_with_dico(2).
# je peux additionner sa valeur avec le résultat de la deuxième branche, et cette valeur sera égale à fib_rec_with_dico(3).
# je pousserai dans le tableau cette valeur la.


dico_fib = {
    0: 0,
    1: 1
}

# print(fib_rec_with_dico(6))


# Consigne : On fait dès le début le test d'arrêt ensuite on teste si la clé n existe dans le dico,
# si oui return la valeur correspondante, sinon on teste si n-1 et n-2 sont des clés du dico,
# si oui, on utilise les valeurs du dico, sinon on demande le calcul en rappelant le fct récursive avec cette valeur.
# Finalement on retourne dico[n-1] + dico[n-2]
# si il fait pas partie du dico tu push, sinon tu utilises sa valeur


def fib_rec_dico2(n):
    if n <= 1:
        return n
    if n in dico_fib:
        return dico_fib[n]
    if n-1 not in dico_fib:
        dico_fib[n-1] = fib_rec_dico2(n-1)
    if n-2 not in dico_fib:
        dico_fib[n-2] = fib_rec_dico2(n-2)
    return dico_fib[n-1] + dico_fib[n-2]

dico = {0: 0, 1: 1}

def fibo_dict_3(n):
    if n not in dico:
        dico[n] = fibo_dict_3(n - 1) + fibo_dict_3(n - 2)
    return dico[n]

print("test de fib_rec_dico2",fib_rec_dico2(11))

# Et pour tester tes fcts, le plus visuel consiste à boucler sur un petit intervalle

for i in range(40):
     print(i,':',fib_rec_dico2(i))


# Exercice 8 : FindMin

tab = [randint(0,100) for _ in range(20)]

print(tab)

def find_min_rec(tab):
    if len(tab) <= 1:
        return tab[0]
    else:
        min_tab_temporaire = find_min_rec(tab[:-1])
        if min_tab_temporaire <= tab[-1]:
            return min_tab_temporaire
        else:
            return tab[-1]

print("le minimun du tableau est:", find_min_rec(tab))

# On va avoir besoin d'une variable min_tab_temporaire qui recevra la valeur de find_min_rec(tab[:-1])
# On va faire le test de notre fonction sur un tableau test tab_test de 3 éléments. tab_test = [49, 12, 28]
# A chaque récursion, on va comparer find_min_rec(tab[:-1]) c'est à dire le tableau amputé d'un élément avec le dernier élément du tableau tab[-1]
# si le minimum du tableau amputé est < à tab[-1], on retourne le tableau amputé, sinon on retourne le dernier élément du tableau
# ici  tab_test = [49, 12, 28]
# PREMIÈRE RENTRÉE DANS LA FONCTION => je vérifie la taille du tableau, elle est supérieure à 1
# je passe dans le else. La variable temporaire min_tab_temporaire recoit = find_min_rec(tab[:-1]) find_min_rec([49, 12])
# à ce moment la, le code de la ligne en dessous de "min_tab_temporaire = find_min_rec(tab[:-1])" ne s'execute pas
# c'est la première récursion (deuxième execution) qui va s'executer avec cette fois ci find_min_rec([49,12])
# len(tab) <= 1 renvoie false, on passe donc à la suite dans le else
#
