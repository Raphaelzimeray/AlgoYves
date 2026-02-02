# from Animal import *
# from Enclos import *
from Zoo import *


a1 = Animal("Marty", "m", 300, "zèbre", 5 * 365)

a2 = Animal("Gloria", "f", 1500, "hippopotame", 7 * 356)


a2.poids -= 50

print(a2.poids)

print(a1.description())

print(a2.description())

print("test de la faim de gloria", a2.faim)

a2.nourrir()

print("test de la faim de gloria après son repas", a2.faim)

a2.faim = 1

a2.nourrir()

print("test de la faim de gloria après son repas", a2.faim)



# Exerice 3

# ici, le voir comme un alias / surnom donné à "a", et pas la création d'un nouvel objet, ou d'une nouvelle instance
a = Animal("Melman", 'm', 1000,"hippopotame",365*8)

b = a

b.poids = 950

print(a.poids)


# Exercice 6


a3 = Animal("Emilie", "f", 290, "zèbre", 5 * 365)


a4 = Animal("Julien", "m", 200, "zèbre", 5 * 365)


a3.nourrir()

a4.nourrir()

bb = a3.reproduction(a4)

print(bb.description())

print("remplissage et création de l'enclos 1")

enclos_1 = Enclos(10, "enclos1")

enclos_1.ajoute(a1)

enclos_1.ajoute(a2)

enclos_1.ajoute(a3)

enclos_1.ajoute(a4)

enclos_1.description()

enclos_1.reproduction()

enclos_1.description()


zooo_1 = Zoo("Nice", [enclos_1])

zooo_1.add_animal_in_zoo(Animal("Jean Michel", "m", 3, "lapin", 5 * 365))

zooo_1.description()

print("Création aléatoire de 5 animaux")

for i in range(5):
    a = Animal.animal_random_creation()
    print(a.description())
