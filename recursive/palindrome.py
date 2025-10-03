# Exercice : on me donne un mot et on doit vérifier si c'est un palindrome

liste_mots = ("kayak", "Radar", "Non", "Nom","coucouc")


# Version récursive
def is_palindrome_rec(word):
    if len(word) <= 1:
        return True
    else:
        return word[0].lower() == word[-1].lower() and is_palindrome_rec(word[1:-1])



# Version itérative
def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i].lower() != word[-1 -i].lower():
            return False
    return True


for mot in liste_mots:
    if is_palindrome_rec(mot):
        print(mot, "est un palindrome")
    else:
        print(mot, 'n \'est pas un palindrome')

# je rentre en ligne 10 avec coucouc
# j'itère autant de fois qu'il y a de lettres // 2 => 7//2 => 3
# si word[0] (c) != word[-1] (c) => je retourne false. ce n'est pas le cas donc je retourne true
#

# Passer de décimale à binaire.
#

