from random import randint
from time import sleep



# Exercice 1 : je fourni en paramètre deux années croisantes, et je veux que ca affiche les années qui vont de l’une à l’autre.
# Fonction récursive à deux paramètres. Comment je fais pour réduire. 1970… 2020.
# None pour dire que ca retourne rien
# Types :int pour typer les variables comme en Typescript et Java

def print_years_rec(year1:int, year2:int)->None:
    if year2 < year1:
        print("Terminé!")
    else:
        print(year1)
        return print_years_rec(year1 + 1, year2)


print(print_years_rec(1800, 1820))

# ok


# Exercice 2 : fonction récursive qui calcule 2 puissance 3 la puissance énième. Fonction a deux paramètres, 2 et n.

def power_rec(n, p):
    if p == 1:
        return n
    else:
        return n * power_rec(n, p-1)


print(power_rec(3, 8))

# ok

# Exercice 3 : Le nombre de chiffre d’un nombres. 1970 => 4

def count_digits(n):
    if n < 1:
        return 0
    else:
        return 1 + count_digits(n//10)


print("test de la fonction count digits exercice 3 :", count_digits(23488))


# décomposer pourquoi un chiffre à 5 digits(23488) retourne 6 et pas 5
# EXECUTION 1 => n<1 => 23488 <1 renvoie false => on passe dans le else
# on retourne 1 + count_digits(n//10) => 1 + count_digits(2348)

# RÉCURSION 1 - EXECUTION 2 => n < 1 => 2348 < 1 renvoie false => on passe dans le else
# on retourne 1 + count_digits(n//10) => total 1 + (1 + count_digits(234))

# RECURSION 2 - EXECUTION 3 => n < 1 => 234 < 1 renvoie false => on passe dans le else
# on retourne 1 + count_digits(n//10) => total 1 + 1 + (1 + count_digits(23))

# RECURSION 3 - EXECUTION 4 => n < 1 => 23 < 1 renvoie false => on passe dans le else
# on retourne 1 + count_digits(n//10) => total 1 + 1 + 1 + (1 + count_digits(n//10))

# RECURSION 4 - EXECUTION 5 => n< 1 => 2 < 1 renvoie false => on passe dans le else
# on retourne 1 + count_digits(n//10) => total 1 + 1 + 1 + 1 + (1 + count_digits(n//10))

# RECURSION 5 - EXECUTION 6 => 0 < 1 => renvoie true => on retourne 1.
# TOTAL 1 + 1 + 1 + 1 + 1 + 1 => 6.
# Soit on retourne 0 dans le if n < 1, soit on retourne 1 si n <=10




print("2//10 =",2//10)



# Exercice 4 : la somme des chiffres d’un nombre. 1970 = 1+9+7+0.

def sum_of_digits_rec(n):
    if n // 10 == 0:
        return n
    else:
        return n%10 + sum_of_digits_rec(n//10)


print("test de la fonction sum of digits rec", sum_of_digits_rec(3324))


# Exercice 5 : Afficher le chiffre de fibonacci

def print_fib_rec(n):
    if n <=1:
        return n
    else:
        return print_fib_rec(n-1) + print_fib_rec(n-2)


print("test de fonction print fib rec", print_fib_rec(3))


# Exercice 6 : Fibonnaci : Optimiser le temps de calcul avec un dictionnaire temporaire


dico_fib = {
    0: 0,
    1:1
}

def print_fib_rec_with_dico(n):
    # if n <= 1:
    #     return n
    if n not in dico_fib:
        dico_fib[n] = print_fib_rec_with_dico(n-1) + print_fib_rec_with_dico(n-2)
    return dico_fib[n]

print("test de la fonction print fib rec with dico", print_fib_rec_with_dico(3))

# ok


# Exercice 7 : Code Wars : Reduce My Fraction


def get_pgcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == 1 or b == 1:
        return 1
    return get_pgcd(b%a, a)



def reduce_fraction(fraction):
    pgcd = get_pgcd(fraction[0], fraction[1])
    result = (fraction[0]/ pgcd, fraction[1]/ pgcd)
    return result




# Exercice 8 : Code Wars : Reduce My Fraction (version itérative)




# Exercice 9 : Vérifier si un mot est un palindrome

list_word = ["kayak", "non", "salut", "cooc", "tot", "rever", "revoir"]

def is_palindrome_rec(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] == word[-1] and is_palindrome_rec(word[1:-1])



# analyse du code avec le mot "cooc", pourquoi ca bloque si on met len(word) ==1

# EXECUTION 1 => len(word) == 1 => 4 == 1 => renvoie false
# on passe dans le bloc else. word[0] == word[-1] => c == c renvoie true et on appelle la fonction récursive
# is_palindrome_rec(word[1:-1]) soit is_palindrome_rec("oo").

# RÉCURSION 1 - EXECUTION 2 => len(word) == 1 => 2 == 1 renvoie false
# on passe dans le bloc else. word[0] == word[-1] => o == o => renvoie true et on appelle la fonction récursive
# is_palindrome_rec(word[1:-1]) soit is_palindrome_rec("")

# RÉCURSION 2 - EXECUTION 3 => len(word) == 1 => 0 == 1 => renvoie false
# on passe dans le bloc else. word[0] == word[-1] => impossible d'accéder aux éléments d'une string vide => erreur
# d'ou la nécessité de mettre la condition d'arrêt à len(word) <=1


for word in range(len(list_word)):
    if is_palindrome_rec(list_word[word]):
        print(list_word[word], "est un palindrome")
    else:
        print(list_word[word], "n'est pas un palindrome")




# Exercice 10 : Trouver le minimum d'un tableau

test_tab = [32, 43, 17, 90, 400, 898, 16, 32, 17]

def find_min_rec(tab):
    if len(tab) <= 1:
        return tab[0]
    else:
        min_tab_temporaire = find_min_rec(tab[:-1])
        if min_tab_temporaire < tab[-1]:
            return min_tab_temporaire
        else:
            return tab[-1]


# print(test_tab[:-1])
# print(test_tab[-1])

# Test sur [4, 1, 5]

# EXECUTION 1 => len(tab) <=1, 3 <= 1 renvoie false, on passe au bloc else
# on déclare min_tab_temporaire qui recoit l'appel de la fonction récursive avec le tableau - le dernier élément
# donc find_min_rec([4,1])

# RÉCURSION 1 - EXECUTION 2 => len(tab) <=1, 2 <= 1 renvoie false on passe au bloc else
# on déclare min_tab_temporaire qui recoit l'appel de la fonction récursive avec le tableau - le dernier élément
# donc find_min_rec([4])

# RÉCURSION 2 - EXECUTION 3 => len(tab) <= 1, 1 <= 1 renvoie true, on return tab[0] ! Et non pas tab tout seul, d'ou l'erreur
# "TypeError: '<' not supported between instances of 'list' and 'int'"
# Maintenant qu'on a corrigé le code (tab[0] au lieu de tab), on a un code qui fonctionne
# La RÉCURSION 2 - EXECUTION 3 à maintenant une valeur de retour (4).

# RETOUR RÉCURSION 1 - EXECUTION 2 => min_tab_temporaire vaut désormais 4.
# if min_tab_temporaire < tab[-1] => 4 < 1, cette condition renvoie false
# on passe dans le else
# on retourne tab[-1] soit 1

# RETOUR EXECUTION 1 => min_tab_temporaire vaut maintenant 1
# if min_tab_temporaire < tab[-1] => 1 < 5, cette condition renvoie true
# on retourne alors min_tab_temporaire (1)

# Le résultat est donc bon, le minimum dans le tableau [4, 1, 5] est bien 1


print("test de la fonction find min rec", find_min_rec(test_tab))



# Exercice 11 : Retrouver le binaire d'un nombre


def dec_to_binary_rec(n):
    if n//2 == 0:
        return str(n%2)
    else:
        return dec_to_binary_rec(n//2) + str(n%2)


print("test de la fonction dec to binary", dec_to_binary_rec(11))

# Décomposition du fonctionnement de la fonction dec_to_binary_rec
# Pourquoi ca fonctionne lorsque je return en dernier dec_to_binary_rec(n//2) + str(n%2),
# Le résultat est différent de lorsque je return str(n%2) + dec_to_binary(n//2)
# Test avec 11 (résultat attendu : 1011) et en dernière ligne return dec_to_binary_rec(n//2) + str(n%2)

# EXECUTION 1 -> dec_to_binary_rec(11). Est ce que 11//2 == 0 (5 == 0) non.
# je passe au bloc else.
# je retourne dec_to_binary_rec(n//2) + str(n%2). Soit dec_to_binary_rec(5) + "1"
# j'appele la fonction récursive dec_to_binary avec 5 en paramètres.

# RÉCURSION 1 - EXECUTION 2 -> dec_to_binary_rec(5). Est ce que 5//2 == 0 (2 == 0). non.
# je passe au bloc else.
# je retourne dec_to_binary_rec(n//2) + str(n%2). Soit(dec_to_binary_rec(2) + "1") + "1" =>
# dec_to_binary_rec(2) + "11"
# j'appelle la fonction récursive dec_to_binary avec 2 en paramètres.

# RÉCURSION 2 - EXECUTION 3 -> dec_to_binary_rec(2). Est ce que 2//2 == 0 (1 == 0). Non.
# Je passe au bloc else.
# Je retourne dec_to_binary_rec(n//2) + str(n%2). Soit (dec_to_binary_rec(1) + "0") + "11"
# dec_to_binary_rec(1) + "011"
# J'appelle la fonction récursive dec_to_binary avec 1 en paramètres.

# RÉCURSION 3 - EXECUTION 4 -> dec_to_binary_rec(1). Est ce que 1//2 == 0 (0 == 0). Oui.
# Je retourne str(n%2) soit "1"

# au total j'ai "1" + "011" => "1011"



# Exercice 12 : Vérifier qu’un tableau de nombre est trié par ordre croissant ou non


# Exercice 13 : Vérifier qu'un nombre est premier

# Un nombre premier est un nombre divisible uniquement par un ou par lui même : 2, 3, 5, 7, 11, 13, 17, 19,

# donc on peut faire un algo qui vérifie si le nombre est divisible par un ou par lui même.
# Qu'est ce qui fait qu'un nombre est premier c'est si je le divise par autre chose que 1 ou lui même, le chiffre sera à virgule
# Quand on prend l'exemple de 11, on voit que seuls 11%1 et 11%11 retournent 0, tout le reste retourne un chiffre.
# Donc pour qu'un nombre soit premier il faut que toutes les divisions qu'on effectue entre 1 et lui même retournent un reste
# != 0. Sinon ca veut dire que la condition n'est pas respectée

def is_prime(n):
    modulo_test = 2
    for i in range(n-2):
        if n% modulo_test == 0:
            return False
        modulo_test +=1
    return True

print("test de la fonction is_prime ", is_prime(20))




# Version Yves avec l'itérateur py

def is_prime2(n):
    if n <2:
        return False
    for modulo_test in range(2,n):
        if n%modulo_test == 0:
            return False
    return True




# Exercice 14 : Code Wars : Tiling Rectangles With squares

# Exemple avec 21 de largeur et 11 de hauteur

# EXECUTION 1 def num_tiles(11, 21):
# Je prend le coté le plus petit du rectangle.
# Tant que le chiffre n puissance 2 < plus petit coté, je continue de boucler (while)
# je récupère n-1 (je suis allé une étape trop haut), exemple 2 ^ 3 = 8 <= 11 je continue, 2 ^4 = 16 <= 11 donc c'est le 2^4 que
# je dois prendre n-1 (3)
# 8x8. ensuite je me pose la question de combien de carrés je peux mettre dans le plus grand coté
# parce que je peux en mettre qu'un seul dans le plus petit coté, sinon c'est qu'il y a un erreur de puissance
# j'ai une puissance trop basse
# division entière de plus grand coté // longeur du carré actuelle
# 21 // 8 => 2 je peux mettre 2 carrés. et il reste 5.
# Je dois ensuite faire le calcul de l'espace qui me reste pour disposer les carrés suivants
# pour calculer l'espace restant, je calcul le % de plus petit coté % taille du carré (11%8) =>3,
# et le % de plus grand coté % taille du carré (21%8) => 5
# j'appelle la fonction récursive avec ces nouveaux paramètres num_tiles(3,5)

# RÉCURSION 1 - EXECUTION 2 - j'appelle la fonction récursive avec ces nouveaux paramètres num_tiles(3,5)
# Tant que le chiffre n puissance 2 < plus petit coté, je continue de boucler (while)
# Je récupère n-1 car je suis allé une étape trop haut. Ici 1 ^ 2 <= 2 => 2 <= 3 ok 2 ^2 <= 3 pas ok 3 <= 4 = false
# donc je retourne n-1 => 1 ^2
# ok dans l'image de l'énoncé je vois qu'il y a deux carrés de 4. Ca veut dire qu'il faut prendre la seconde fois le coté le plus
# grand du rectangle en référence pour calculer la taille du ou dés carrès que l'on va insérer à l'intérieur
