from propagation_fonctions import *

# execution du script
sol = getSol("data/propagation.txt")

for ligne in sol:
    print(ligne)

# on


# EXEMPLE AVEC un tableau de 2 dimensions
tab2d = [[0, 1, 2, 3], [4, 5, 6]]

# for l in tab2d:
#     print(l)

print("test de tab2d[1][1]: ",tab2d[1][1])
# print("test de len tab",len(tab2d))


for l in range(len(tab2d)):
    for c in range (len(tab2d[l])):
        print(tab2d[l][c], end= " ")
    print("")

# Appel de la fonction search

search(sol)

# re affichage du fichier

for ligne in sol:
    for col in ligne:
        print(col, end=" ")
    print("")
