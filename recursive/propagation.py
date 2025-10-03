# on peut l'afficher en mode matrice en 2 dimensions, un certain nombre de lignes et un certain nombre de colonnes
# chaque lignes à le même nombre de caractères
# il y a un \n pour faire le retour à la ligne
# une matrice c'est une liste de liste, c'est une liste de dimension 2. Chaque élément du tableau est une liste.
# pour charger un fichier .txt !=json or csv
# utf-8 vs utf-16 (c'est le nombre d'octet dans lequel est codé un caractère) Unified text formating. En général utf-8
#
terrain = []
file_name = "data/propagation.txt"
with open (file_name, "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        terrain.append(list(ligne[:-1]))

for ligne in terrain:
    print("".join(ligne))

print(terrain)


def fill_terrain(terrain:list)->None:
    value = 1
    for l in range(len(terrain)):
        for c in range(len(terrain[0])):
            if terrain[l][c] == "X":
                terrain[l][c] = "."
            if terrain[l][c] == " ":
                propagation(terrain, l, c, value)
                value +=1



# une fonction va s'occuper de la propagation
# l'autre va s'occuper du terrain de facon plus large


def propagation(terrain, l, c, value):
    if 0 <= l < len(terrain) and 0 <= c < len(terrain[0]) and terrain[l][c] == " ":
        terrain[l][c] = str(value)
        propagation(terrain, l-1, c, value)
        propagation(terrain, l+1, c, value)
        propagation(terrain, l, c-1, value)
        propagation(terrain, l, c+1, value)


fill_terrain(terrain)


print(" ")
for ligne in terrain:
    # print(ligne)
    print("".join(ligne))
