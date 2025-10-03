# Tri quadratique (parce que c'est en n2, deux boucles for imbriquées)
# Tri à bulles

# tableau de 20 éléments à trier en ordre croissant



def permute(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]
