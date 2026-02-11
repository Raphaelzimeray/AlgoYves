from Batiment import *
from Immeuble import *
from Maison import *
from Quartier import *
# import Batiment, Immeuble, Maison


#Batiment

batiment_1 = Batiment("42 rue des Lilas", 50)
# Maison

maison_1 = Maison("28 rue de l'Eglise", 25, 4, 200)

# Immeuble

immeuble_1 = Immeuble("12 avenue Victor Hugo", 400, 5)


list_de_batiments = [batiment_1, maison_1, immeuble_1]

for batiment in list_de_batiments:
    print(batiment)


# Quartier

quartier_1 = Quartier()

for batiment in list_de_batiments:
    quartier_1.add_batiment(batiment)

print(" Affichage des batiments du quartier après son remplissage par add_batiment")

# Malgré le fait que la liste des édifices du quartiers soient définies en batiments dans le constructeur du quartiers,
# les enfants sont acceptés sans difficutés

for b in quartier_1.list_batiments:
    print(b)


# tests de la catégorie

for b in quartier_1.list_batiments:
    print(b, "Catégorie: ", b.get_category())


# test du display category

print("Test du display category")

quartier_1.display_category(2)
