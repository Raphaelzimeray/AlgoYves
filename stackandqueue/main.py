from Pile import *

pile_1 = Pile(10)

# Ajout de 10 éléments

for i in range(1, 11):
    pile_1.stack(i)

# affichage

print(pile_1)


# Afficher l'élément au sommet

print("element au sommet :", pile_1.get_top())


# Supprimer un élément

pile_1.unstack()

# Ré affichage (avec un élément de moins normalement)

print(pile_1)



# Exercice 1 : Ranger les éléments en ordre inverse dans une nouvelle pile (pile initiale deviens vide). Je travaille sur la liste
# mais avec les méthodes autorisées par le créateur de la classe

def reverse_stack(pile:Pile) -> Pile:
    pile2 = Pile(pile.taille_max)
    while not pile.is_empty():
        pile2.stack(pile.unstack())
    return pile2



p2 = reverse_stack(pile_1)

print("test pile 2 \n", p2)
print("test pile 1 \n",pile_1)


for i in range(1, 11):
    pile_1.stack(i)

# Exercice 2 : Ranger les éléments en ordre inverse dans une nouvelle pile (pile initiale conservée)

def reverse_stack_2(pile:Pile) -> Pile:
    pile2 = Pile(pile.taille_max)
    pile3 = Pile(pile.taille_max)
    while not pile.is_empty():
        pile3.stack(pile.get_top())
        pile2.stack(pile.unstack())
    while not pile3.is_empty():
        pile.stack(pile3.unstack())
    return (pile2)


p2 = reverse_stack_2(pile_1)

print("test de pile 2 après reverse stack 2 \n", p2)
print("test de pile 1 après reverse stack 2 \n", pile_1)


# Exercice 3 : Vérifier si l'expression numérique est correctement parenthésée (parenthèses mises de facon logique). Il y aura
# les parenthèses, les crochets, et accolades (), [], {}.

numerical_expression = "(x + [2 * {[3/(25 - sqrt(9))] - cos(1.54)}])"

# je pars de la gauche et j'analye le caractère. Les seuls caractères qui m'intéressent sont ()[]{}. Si c'est un (, je la mets dans la pile
# si c'est un autre caractère quelconque je ne fais rien. et si c'est une parenthèse fermante alors je verifie que le top de ma pile est une
# parenthèse ouvrante.

pile_letters = Pile(10)

for i in range(1, 11):
    pile_letters.stack("coucou")

print("test de pile letters", pile_letters)

numerical_expression2 = "(x + [2 * {[3/(25 - sqrt(9))] - cos(1.54)}]))"


def check_numeric_syntax(expression:str) -> bool:
    pile_expression = Pile(len(expression))
    dico_tag = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
    }
    for c in expression:
        if c in dico_tag.values():
            pile_expression.stack(c)
        elif c in dico_tag:
            if dico_tag[c] == pile_expression.get_top():
                pile_expression.unstack()
            else:
                return False
    return pile_expression.is_empty()
    # if pile_expression.is_empty():
    #     return True
    # else:
    #     return False



print("test de check numeric syntax", check_numeric_syntax(numerical_expression))

print("test de check numeric syntax", check_numeric_syntax(numerical_expression2))
