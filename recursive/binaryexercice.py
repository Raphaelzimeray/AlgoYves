# Passer de décimale à binaire.
# je peux tenter l'exercice en fonction récursive

# Version itérative

# On chiffre est donné en entrée (ex: 586)
# 1 - On divise le nombre à convertir par 2, et on note le reste de la division (ici 0)
# 2 - On divise le quotient (résultat) (293) de la division précédente par 2 (reste 1)
# 3 - même chose 146 / 2 => 73 quotient 0
# on s'arrête quand le quotien est nul
# on peut stocker dans un tableau chaque reste de la division à chaque fois qu'on l'effectue (dec_write)
# Dans notre cas on divise le nombre par deux à chaque tour de boucle
# si n/2 = 0 on arrête

def convert_dec_to_binary(num):
    binary_num = []
    while num //2 != 0:
        binary_num.append(num%2)
        num = num // 2

    if num//2 == 0:
        binary_num.append(num%2)
    binary_num.reverse()
    int_list_str = [str(element) for element in binary_num]
    joined_str = "".join(int_list_str)
    return joined_str


print("voici le chiffre en binaire VERSION IT", convert_dec_to_binary(10))

# Remarque du professeur sur le poids des variables :
# Tu constateras que 2^8 = 256 = 100000000 donc 255 = 11111111 soit 8 bits de 1 soit 1 octet.

# for i in range (10):
#     print(2**i, " en décimal, ca fait", convert_dec_to_binary(2**i), " en binaire !")


# Version fonction récursive
# La condition false de notre while dans la version itérative va devenir notre condition d'arrêt
# Notre condition d'arrêt c'est donc que en divisant l'élément passé en paramètres par 2 dans une division entière,
# On obtienne 0
# Si c'est le cas on retournera le %2 du chiffre passé en paramètre
# Pour le bloc else, je me pose la question de savoir ce que je sait à l'état n-1 pour obtenir l'état n
# je sais qu'a l'état n-1 j'ai un chiffre (ex586) => comment je fais faire pour qu'à l'état n, j'obtienne
# 293 ?
#


def dec_2_bin_rec(num):
    if num // 2 == 0:
        return num
    else:
       return dec_2_bin_rec(num//2) + str(num%2)


# for i in range(10):
#     print("voici le chiffre", i, "en binaire", convert_dec_to_binary_rec(i))

# for i in range (10):
#     print(2**i, " en décimal, ca fait", convert_dec_to_binary(2**i), " en binaire !")



# Il manque un élément dans le string retourné, un 0. Résultat attendu : 1001001010, Résultat recu : 100100101
# sans le reverse le tableau retourné est
# Comment faire ? décomposition

# PREMIÈRE EXECUTION DE LA FONCTION avec 10
# est ce que 10 // 2 == 0, non la condition renvoie false
# je passe dans le bloc else
# je pousse dans le tableau tab_binary=[] num%2 => 10%2 => 0 => ici tab_binary = [0]
# je retourne l'appel de la fonction convert_dec_to_binary(num//2) => convert_dec_to_binary(10//2) => convert_dec_to_binary(5)

# PREMIÈRE RÉCURSIVITÉ, 2E EXECUTION DE LA FONCTION avec 5
# est ce que 5//2 == 0, non la condition renvoie false
# je passe dans le bloc else
# je pousse dans le tableau tab_binary=[] num%2 => 5%2=> 1 => ici tab_binary = [0,1]
# je retourne l'appel de la fonction récursive convert_dec_to_binary(num//2) => convert_dec_to_binary(5//2) => convert_dec_to_binary(2)

# DEUXIÈME RÉCURSIVITÉ, 3 E EXECUTION DE LA FONCTION AVEC 2
# est ce que 2 // 2 = 0, non, la condition renvoie false
# je passe dans le bloc else
# je pousse dans le tableau tab_binary=[] num%2 => 2%2 => 0 => ici tab_binary = [0, 1, 0]
# je retourne l'appel de la fonction récursive convert_dec_to_binary(num//2) => convert_dec_to_binary_(2//2) => convert_dec_to_binary(1)

# TROISIÈME RÉCURSIVITÉ, 4 E EXECUTION DE LA FONCTION AVEC 1
# est ce que 1//2 = 0, oui, la condition renvoie true
# je passe dans le bloc if, je pousse dans mon tableau tab_binary=[] num(1%2) => 1 => ici tab_binary = [0, 1, 0, 1]
# si j'applique un reverse sur ce tableau j'obtiens [1, 0, 1, 0]



# print(1//2)
