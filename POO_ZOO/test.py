from Animal import *


a1 = Animal("Marty", "m", 300, "Zèbre", 5 * 365)

a2 = Animal("Gloria", "f", 1500, "Hippopotame", 7 * 356)


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
a = Animal("Melman", 'm', 1000,"girafe",365*8)

b = a

b.poids = 950

print(a.poids)


# Exercice 6


a3 = Animal("Emilie", "f", 350, "Zèbre", 5 * 365)


a4 = Animal("Julien", "m", 500, "Zèbre", 5 * 365)


a3.nourrir()

a4.nourrir()

bb = a3.reproduction(a4)

print(bb.description())
