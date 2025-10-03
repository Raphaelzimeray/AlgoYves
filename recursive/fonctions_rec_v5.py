from random import randint
from time import sleep

tab_test = [randint(0,100) for _ in range(20)]

print(tab_test)


# Exercice trouver le minimun d'un tableau

def find_min_rec(tab):
    if len(tab) <= 1:
        return tab[0]
    else:
        min_tab_temporaire = find_min_rec(tab[:-1])
        if min_tab_temporaire < tab[-1]:
            return min_tab_temporaire
        else:
            return tab[-1]


print("test du minimun de la table", find_min_rec(tab_test))


# Pourquoi ca marche ? Explications test sur une table exemple tab_ex = [23, 4, 12]
# PREMIÈRE EXECUTION DE LA FONCTION => Est ce que je rentre dans le if ? non (3 n'est pas <=1).
# ligne 15, je crée une variable qui recoit l'appel de la fonction find_min_rec(tab[:-1]),
# on appelle find_min_rec avec le tableau amputé d'un élément => [23, 4]
# ON RENTRE DANS LA PREMIÈRE RÉCURSION (2 e execution de la fonction) => Est ce que je rentre dans le if ? non (2 n'est pas <=1)
# j'arrive de nouveau ligne 15 de cette deuxième fonction, et je crée une variable min_tab_temporaire(2) propre à cette première
# poupée russe
# J'appelle donc find_min_rec([23])
# ON RENTRE DANS LA DEUXIÈME RÉCURSION (3 e execution de la fonction) => Est ce que je rentre dans le if ? Oui (1 <= 1)
# Je retourne tab[0] => 23
# Je repars dans l'autre sens, maintenant, je remonte d'un cran dans les poupées russes (j'était dans la 2e, je vais dans la 1ere)
# ON REVIENS DANS LA PREMIÈRE RÉCURSION
# Maintenant, min_tab_temporaire vaut 23. Je peux passer à la suite de l'execution du code puisque j'ai ma réponse
# je regarde si min_tab_temporaire (23) < tab[-1] (4).
# Cette condition renvoie false, donc je passe dans l'alternative (bloc else) et je return 4.
# Je monte encore d'un cran et j'arrive dans la mère des poupées russes
# ON EST REVENUS DANS LA PREMIÈRE EXECUTION DE LA FONCTION => Ici, comme dans les enfants, j'était bloqué en ligne 15
# Je vais donc pouvoir avoir une valeur dans ma varible min_tab_temporaire (4, le retour du resultat de la première poupée russe)
# Je regarde si 4 < 12 (tab[-1])
# Cette condition renvoie true, donc je rentre dans le bloc if, et j'ai la valeur de retour return min_tab_temporaire qui vaut 4
# Le minimum est donc 4


# Est ce qu'un mot est un palindrome

list_of_words = ["kayak", "coucou", "Non", "Weeueew", "Radar", "salut"]


def is_palindrome(word):
    if len(word) == 1:
        return True
    else:
        print("je rentre ici?")
        return word[0].lower() == word[-1].lower() and is_palindrome(word[1:-1])



for i in range(len(list_of_words)):
    if is_palindrome(list_of_words[i]):
        print(list_of_words[i], "est un palindrome")
    else:
        print(list_of_words[i], "n'est pas un palindrome")


