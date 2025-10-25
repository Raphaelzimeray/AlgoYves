# Exercice 16 : Propagation (avec le fichier propagation.txt, remplir l'élément de "1" et de "2")

# on peut l'afficher en mode matrice en 2 dimensions, un certain nombre de lignes et un certain nombre de colonnes
# chaque lignes à le même nombre de caractères
# il y a un \n pour faire le retour à la ligne
# une matrice c'est une liste de liste, c'est une liste de dimension 2. Chaque élément du tableau est une liste.
# pour charger un fichier .txt !=json or csv
# utf-8 vs utf-16 (c'est le nombre d'octet dans lequel est codé un caractère) Unified text formating. En général utf-8

def search(tab:list) -> None:
    valeur = 1
    for ligne in range(len(tab)):
        for colonne in range(len(tab[ligne])):
            if tab[ligne][colonne] == " ":
                propagation(tab, ligne, colonne, valeur)
                valeur +=1





def propagation(tab:list, l:int, c:int, val:int) -> None:
    if 0 <= l < len(tab) and 0 <= c < len(tab[l]) and tab[l][c] == " ":
        tab[l][c] = val
        propagation(tab, l+1, c, val)
        propagation(tab, l-1, c, val)
        propagation(tab, l, c -1, val)
        propagation(tab, l, c + 1, val)




def getSol(file_name:str) -> list:
    sol = []
    with open(file_name, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            sol.append(list(ligne[:-1]))
    for ligne in range(len(sol)):
        for col in range(len(sol[ligne])):
            if sol[ligne][col] == "X":
                sol[ligne][col] = "-"
    return sol
