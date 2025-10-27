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


# Exercice 2 : Ranger les éléments en ordre inverse dans une nouvelle pile (pile initiale conservée)

def reverse_stack_2(pile:Pile) -> Pile:
    pile2 = Pile(pile.taille_max)
