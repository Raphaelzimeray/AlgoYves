# trouve le chiffre le plus petit dans une liste

from random import randint
from time import sleep

tab = [randint(0,100) for _ in range(20)]

print(tab)


# je connais la réponse qui vaut n-1 en récursive. le n sera la taille du tableau
# je vais décroitre la taille de mon tableau à chaque fois de 1
# le min d'un tableau de taille n (tab.length en js len(tab))(la dimension du tableau)
# la formule c'est min_rec(tab) return min(min_rec(tab[:-1]), tab[-1])
niveaurecursion = 0

def find_min_rec(tab):
    global niveaurecursion
    if len(tab) == 1:
        return tab[0]
    else:
        mintabtemporaire = find_min_rec(tab[:-1])
        sleep(1)
        print(niveaurecursion, mintabtemporaire)
        niveaurecursion+=1
        if mintabtemporaire <= tab[-1]:
            return mintabtemporaire
        else:
            return tab[-1]

print("test du resultat", find_min_rec(tab))

# sur le tableau [55, 32, 70, 93]
# au départ on rentre pas dans le if, on passe le else, et la variable
# mintabtemporaire recoit = find_min_rec([55, 32, 70]) donc l'appel de la fonction mintabtemporaire
# je ne vais pas executer ce qu'il y a en dessous, je l'executerai à la fin quand find_min_rec aura retourné un resultat
# on re rentre dans la fonction (1 ère récursion)
# on arrive dans le else bien sur et on crée une nouvelle variable mintabtemporaire(2) dont le scope
# se limite à la première récursion uniquement. Cette nouvelle variable recoit find_min_rec([55, 32])
# On rentre maintenenant dans la fonction (2e récursion)
# on arrive dans le else, taille du tableau c'est 2, on crée une nouvelle variable mintabtemporaire(3) dont le scope
# se limite à la deuxième récursion uniquement. Cette nouvelle variable recoit find_min_rec(55)
# on rentre dans la troisième récursion, je rentre dans le if, la taille de mon tableau est = 1
# et la fonction retourne le seul élément du tableau tab[0] (dans notre cas 55)
# On doit trouver qui recoit 55, quelle variable recoit 55 ? C'est ligne 35 mintabtemporaire(3)
# je remonte d'un cran dans la récursion et je reviens dans la deuxième récursion.
# Donc la, j'ai mintabtemporaire(3) = 55
# je vais pouvoir executer la suite de mon code, si  mintabtemporaire(3) <= tab[-1]: donc si => 55 <= 32
# je teste la condition du if, et la réponse c'est false
# donc je vais dans le else, et je return 32 (tab[-1]).
# Dans quelle variable va aller 32 ?
# Je vais donc remonter d'un cran et repartir dans ce qu'on appelle la première récursion
# Maintenant, je suis fixé sur mintabtemporaire(2), il faut 32.
# est ce que mintabtemporaire(2) <= tab[-1] (à un stade de récursion ou le tableau est composé de 3 éléments)
# on test si 32 <= 78. Ce test renvoie true, on passe dans le if
# on retourne donc la valeur mintabtemporaire(2) (ici 32) à la fonction suivante
# maintenant je reviens dans la première version de la fonction, la mères des poupées russes.
# je compare mintemporaire(v1) <=tab[-1]
# je test si 32 <=93. Ce test renvoie true, on passe dans le if
# je retourne mintemporaore(v1) c'est la fin de la fonction. Donc ca renvoie 32.
