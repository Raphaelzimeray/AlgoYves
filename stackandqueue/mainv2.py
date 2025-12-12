# Exercice 1 : Ranger les éléments en ordre inverse dans une nouvelle pile (pile initiale deviens vide). Je travaille sur la liste
# mais avec les méthodes autorisées par le créateur de la classe

from Pilev2 import *

from random import randint

pile1 = Pile(10)

for i in range(1, 11):
    pile1.stack(i)

print(pile1)

pile1.reverse_stack()

print(pile1)

pile2 = Pile(10)

for i in range(1, 11):
    pile2.stack(randint(0, 200))

print("test de la pile 2 avant qu'elle soit inversée", pile2)

print("test du max de la pile", pile2.max())

print("test de partial max", pile2.partial_max(4))

print("test de l'index du max d'une partie de la pile", pile2.partial_max_index(4))

pile2.partial_reverse(4)

print("test de la pile 2 après que ses 4 premiers éléments aient été inversés", pile2)

def reverse_stack(pile:Pile) -> Pile:
    pile_temp = Pile(pile.taille_max)
    while not pile.is_empty():
        pile_temp.stack(pile.unstack())
    return pile_temp



pile3 = Pile(15)

for i in range(1, 10):
    pile3.stack(randint(0, 20))


print("Test de la pile 3 avant qu'elle soit inversée par la fonction hors classe", pile3)

reverse_stack(pile3)

print("Test de la pile 3 après qu'elle soit inversée par la fonction hors classe", pile3)

print("test de la taille de la pile", pile3.number_of_elements())

pile3.order_elements()

print("Test de la pile 3 après qu'elle soit rangée par order elements", pile3)


pile5 = Pile(10)


for i in range(1, 10):
    pile5.stack(randint(0, 20))


print("Test PILE 5 avant partial reverse(4) \n", pile5)

pile5.partial_reverse(4)

print("Test PILE 5 après partial reverse(4) \n", pile5)



# Exercice 2 : Ranger les éléments en ordre inverse dans une nouvelle pile (pile initiale conservée)
# a faire

def reverse_stack_2(pile:Pile) -> Pile:
    pile2 = Pile(pile.taille_max)
    pile3 = Pile(pile.taille_max)
    while not pile.is_empty():
        pile3.stack(pile.get_top())
        pile2.stack(pile.unstack())
    while not pile3.is_empty():
        pile.stack(pile3.unstack())
    return pile2



pile6 = Pile(12)

for i in range(1, 10):
    pile6.stack(randint(0, 20))

print("test de la pile 6 avant reverse_stack2", pile6)

print(reverse_stack_2(pile6))

print("test de la pile 6 après reverse_stack2", pile6)




# Exercice 3 : Vérifier si l'expression numérique est correctement parenthésée (parenthèses mises de facon logique). Il y aura
# les parenthèses, les crochets, et accolades (), [], {}.

numerical_expression = "(x + [2 * {[3/(25 - sqrt(9))] - cos(1.54)}])"

numerical_expression2 = "(3 + [5 * 2) - 4]"

numerical_expression3 = "(3 + [5 * (2 + 4)]) - {7 / (1 + 6)}"




# print("test de la taille de l'expression numérique", len(numerical_expression))


# je pars de la gauche et j'analye le caractère. Les seuls caractères qui m'intéressent sont ()[]{}. Si c'est un (, je la mets dans la pile
# si c'est un autre caractère quelconque je ne fais rien. et si c'est une parenthèse fermante alors je verifie que le top de ma pile est une
# # parenthèse ouvrante.

# pile_letters = Pile(10)

# for i in range(1, 11):
#     pile_letters.stack("coucou")

# print("test de pile letters", pile_letters)

# numerical_expression2 = "(x + [2 * {[3/(25 - sqrt(9))] - cos(1.54)}]))"

numerical_expression4 = "(([])"


def check_numeric_syntax(expression:str) -> bool:
    tags = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    pile_tags = Pile(len(expression))
    for char in expression:
        if char in tags.values():
            pile_tags.stack(char)
        if char in tags:
            print("je rentre dans ce if ?")
            print(tags.get(char))
            if tags.get(char) != pile_tags.get_top():
                return False
            pile_tags.unstack()
    return pile_tags.is_empty()



print("Test de check numeric syntax avec numerical expression 4", check_numeric_syntax(numerical_expression3))



# Exercice 4 : Crêpes. Il y a une pile de crêpes, chaque crêpes à un diametre, il veut ranger la plus grande en bas et la plus petite en haut.
# Il a le droit uniquement de prendre sa spatule la ou il veut sous une crêpe et de retourner l'ensemble
# à partir de ca, du haut jusqu'à la crêpe il doit retourner l'ensemble.
# Il ne peut retourner que les crêpes qui sont au dessus de sa spatule. Il inverse l'ordre des crêpes au dessus de sa spatule.
# retourner la crepe la plus grande parmis p crêpes (dans un range). et ensuite comment j'inverse p crêpes. les deux sont des méthodes de la classe pile


# test de max

# pile4 = Pile(10)

# for _ in range(8):
#     pile4.stack(randint(0, 100))


# print(pile4)

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
    pass


# Exercice 5 : Faire une sorte de mini calculatrice

# https://fr.wikipedia.org/wiki/Notation_polonaise_inverse


operation1 = "10 5 - 3 /"

# dans le cas ou on a plusieurs éléments à additionner, il faut aux additions
# successives qui se réalisent

op1 = "13 14 10 5 + + +"
op2 = "13 14 + 10 + 5 +"
op3 = "13 14 + 10 5 + +"

def calculator(expression:str):
    pass
