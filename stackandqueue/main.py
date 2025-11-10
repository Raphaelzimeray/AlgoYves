from Pile import *

from random import randint

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


# Exercice 4 : Crêpes. Il y a une pile de crêpes, chaque crêpes à un diametre, il veut ranger la plus grande en bas et la plus petite en haut.
# Il a le droit uniquement de prendre sa spatule la ou il veut sous une crêpe et de retourner l'ensemble
# à partir de ca, du haut jusqu'à la crêpe il doit retourner l'ensemble.
# Il ne peut retourner que les crêpes qui sont au dessus de sa spatule. Il inverse l'ordre des crêpes au dessus de sa spatule.
# retourner la crepe la plus grande parmis p crêpes (dans un range). et ensuite comment j'inverse p crêpes. les deux sont des méthodes de la classe pile


# test de max

pile4 = Pile(10)

for _ in range(8):
    pile4.stack(randint(0, 100))


print(pile4)

# print("test de max de pile 4", pile4.max())

# print("test de partial max de pile 4", pile4.partial_max(4))

# pile4.partial_reverse(4)

# print("test de partial reverse de pile 4", pile4)

# max_index_1 = pile4.partial_max_index(pile4.number_of_elements())

# print("test de max index 1", max_index_1)

# # inverser la pile jusqu'à la position de la plus grande crêpe

# pile4.partial_reverse(max_index_1)

# print(pile4)

# pile4.partial_reverse(pile4.number_of_elements())

# print(pile4)

def order_elements(pile:Pile):
    i = pile.number_of_elements()
    while i > 0:
        j = pile.partial_max_index(i)
        pile.partial_reverse(j)
        pile.partial_reverse(i)
        i -=1

# order_elements(pile4)

pile4.order_elements()

print("test de order elements", pile4)


# Exercice 5 : Faire une sorte de mini calculatrice

# https://fr.wikipedia.org/wiki/Notation_polonaise_inverse


operation1 = "10 5 - 3 /"

# dans le cas ou on a plusieurs éléments à additionner, il faut aux additions
# successives qui se réalisent

op1 = "13 14 10 5 + + +"
op2 = "13 14 + 10 + 5 +"
op3 = "13 14 + 10 5 + +"

def calculator(expression:str):
    operation_list = expression.split(" ")
    pile_operation = Pile(len(operation_list))
    for elt in operation_list:
        if elt not in ("+", "/", "-", "*"):
            pile_operation.stack(elt)
            print("pile: ", pile_operation)
        else:
            print("operator : ", elt)
            a = float(pile_operation.unstack())
            b = float(pile_operation.unstack())
            if elt == "+":
                pile_operation.stack(a+b)
            elif elt == "-":
                pile_operation.stack(b-a)
            elif elt == "*":
                pile_operation.stack(a*b)
            elif elt == "/":
                pile_operation.stack(b/a)
            print("pile: ", pile_operation)
    return pile_operation.unstack()



print(operation1)
res = calculator(operation1)
print("test de calculator(operation1)", res)

print("expression à calculer : ", op1)
res = calculator(op1)
print("résultat:", res)

print("expression à calculer : ", op2)
res = calculator(op2)
print("résultat:", res)

print("expression à calculer : ", op3)
res = calculator(op3)
print("résultat:", res)



# calculator(operation1)


