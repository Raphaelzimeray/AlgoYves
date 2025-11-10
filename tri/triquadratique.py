# Tri quadratique (parce que c'est en n2, deux boucles for imbriquées)
# Tri à bulles

# tableau de 20 éléments à trier en ordre croissant
from random import randint
from time import time
from matplotlib import pyplot as plt

def permute(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]


tab_unsorted = [randint(0,100) for _ in range(50)]
print(" intro tri")
print(tab_unsorted)

# parcourir le tableau jusqu'à trouver le minimum et quand on le trouve on le met au début



def sort_tab(tab):
    tab_sorted = tab[:]
    for j in range(len(tab_sorted) - 1):
        min_value_index = j
        for i in range(j, len(tab_sorted)):
            if tab_sorted[i] < tab_sorted[min_value_index]:
                min_value_index = i
        permute(tab_sorted, j, min_value_index)
    return tab_sorted



def bubble_sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-1 - i):
            if tab[j] > tab[j+1]:
                permute(tab, j, j+1)



def bubble_sort2(tab):
    for i in range(len(tab)):
        indice_val_max = i
        for j in range(len(tab)-1 - i):
            if tab[j] > tab[indice_val_max]:
                indice_val_max = j
        permute(tab, len(tab) -1 -i, indice_val_max)


# Tri par insertion

def insert_sort(tab):
    for i in range(1, len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j -1]
            j = j - 1
        tab[j] = x



print("test du tri par insertion", insert_sort(tab_unsorted))
print("test de tab unsorted apres la fonction insert sort", tab_unsorted)

# Décomposition du code de insert sort avec un tableau à 4 éléments
# tab_test = [32, 7, 98, 3]

# Je rentre dans la fonction, on boucle autant de fois qu'il y a
# d'éléments dans le tableau
# il faut commencer le i a 1 parce que on va comparer le 2 e element au premier élément

# TOUR DE BOUCLE FOR N1, i = 1
# la variable x recoit tab[i] donc tab[1] = 7. x = 7
# la variable j recoit i donc 1 donc j = 1
# TOUR BOUCLE WHILE N1,
# tant que j > 0 parce que un indice ne peut pas etre inférieur à 0
# et on calcul tab[j-1] on va comparer la valeur de tab[j-1] avec x
# donc ici 32 avec 7
# donc pour rentrer dans cette boucle il faut que j soit > 0 et que
# l'élément a gauche du tableau soit supérieur a x
# ici j > 0 => 1 > 0 ca renvoie true
# tab[j-1] > x =>  tab[1-1] > x => tab[0] > 7 => 32 > 7. ca renvoie true aussi
# je rentre dans mon while, j'arrive en ligne 57 et je remplit tab[j] avec tab[j-1]
# donc tab[1] = tab[0]
# donc tab[1] = 32
# donc a cet instant le 7 est soulevé dans la ram dans x, et le tableau vaut [32, 32, 98, 3]
# je décrémente j. donc j - 1 => 1 - 1 = 0.
# Je sors de la boucle while et je dis que tab[j] recoit x donc tab[0] = 7.
# donc on a à ce stade un tableau qui fait [7, 32, 98, 3]
# donc il est déjà un peu rangé.

# TOUR DE BOUCLE FOR N2, i = 2
# la variable x recoit tab[i] donc 98
# la variable j recoit i donc 2 donc j = 2
# TOUR DE BOUCLE WHILE N2.1
# tant que j > 0 et que tab[j-1] > x
# 2 > 0 ok tab[1] > x  => 32 > 98 nok (not ok)
# donc une des 2 conditions de la boucle while n'est pas satisfaite
# je ne rentre pas dedans, et je vais directement en ligne 59 tab[j] = x
# tab[2] = 98, donc 98 = 98. donc je l'ai soulevé et je l'ai reposé
# j'a toujours le même tableau inchangé [7, 32, 98, 3]

# TOUR DE BOUCLE FOR N3, i = 3
# la variable x recoit tab[i] donc tab[3] donc 3
# la variable j recoit i donc 3 donc j = 3
# TOUR DE BOUCLE WHILE N3.1
# 3 > 0 ok tab[2] > x 98 > 3 ok, les deux conditions sont satisfaites donc je peux rentrer dans la boucle while
# je commence les décalages tab[j] = tab[j -1]
# tab[3] <- tab[2] donc tab[3] <-98
# donc le tableau ici c'est temporairement 2 fois les mêmes valeurs [7, 32, 98, 98]
# je décrémente j, qui passe de 3 à 2. (j-1) j = 2
# TOUR DE BOUCLE WHILE N3.2
# 2 > 0 ok tab[1] > x  => 32 > 3 ok, les deux conditions sont satisfaites donc je peux rentrer dans la boucle while
# je continue les décalages tab[j] <- tab[j- 1]
# tab[2] <- 32 donc tab [2] est égal à 32
# donc le nouveau tableau c'est temporairement [7, 32, 32, 98]
# je décrémente j qui passe de 2 à 1 (j-1) j = 1
# TOUR DE BOUCLE WHILE N3.3
# 1 > 0 ok tab[j-1] > x => tab[0] > 3 => 7 > 3 ok c'est bon les deux conditions sont satisfaites je rentre dans le while
# je continue les décalages
# tab[1] <- tab[1-1] donc tab[1] <- 7
# donc le nouveau tableau c'est temporairement [7, 7, 32, 98]
# je décrémente qui passe de 1 à 0. (j-1) j = 0
# TOUR DE BOUCLE WHILE N3.4
# 0 > 0 nok donc impossible de rentrer dans cette boucle while
# ca fait 3 tour de boucle while que je n'ai pas touché à la ligne 59, celle
# d'après la boucle while, tab[j] = x
# donc tab[0] = 3
# donc j'ai le tableau suivant [3, 7, 32, 98]
# mon tableau est trié
# mon i vaut 3 et len(tab) = 4. donc sur un tableau de 4 éléments
# donc sur 1, len(tab) = 4 , i = 1, 2, 3


# Tri par séléction

#tab_test = [56, 12, 9, 3]

def select_sort(tab):
    for i in range(len(tab) -1):
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        tab[min], tab[i] = tab[i], tab[min]


# Tri par séléction avec test d'égalité

def select_sort2(tab):
    for i in range(len(tab) -1):
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        if min != i:
            tab[min], tab[i] = tab[i], tab[min]


def select_sort3(tab):
    i = 0
    is_sorted = False
    while not is_sorted and i < len(tab) -1:
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        if min != i:
            tab[min], tab[i] = tab[i], tab[min]
        else:
            is_sorted = True
        i +=1



tab_sorted = sort_tab(tab_unsorted)
print(tab_sorted)
print(tab_unsorted)


min = 100
max = 5000
step = 100

X = [x for x in range(min, max, step)]

Y = []



for i in range (min, max, step):
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    start = time()
    f = sort_tab(tab_unsorted)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='tri basique')

Y = []



for i in range (min, max, step):
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    start = time()
    f = bubble_sort(tab_unsorted)
    stop = time()
    Y.append(stop - start)


plt.plot(X,Y,label='tri a bulle')

Y = []



# for i in range (min, max, step):
#     tab_unsorted = [randint(0,i//2) for _ in range(i)]
#     start = time()
#     f = bubble_sort2(tab_unsorted)
#     stop = time()
#     Y.append(stop - start)

# plt.plot(X,Y,label='tri a bulle optimisé')


# Y = []


for i in range (min, max, step):
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    # tab_unsorted.sort()
    # permute(tab_unsorted, 5, len(tab_unsorted)-5)
    start = time()
    f = insert_sort(tab_unsorted)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='tri par insertion')

Y = []


for i in range (min, max, step):
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    tab_unsorted.sort()
    permute(tab_unsorted, 5, len(tab_unsorted)-5)
    start = time()
    f = select_sort(tab_unsorted)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='tri par selection')

Y = []


for i in range (min, max, step):
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    tab_unsorted.sort()
    permute(tab_unsorted, 5, len(tab_unsorted)-5)
    start = time()
    f = select_sort2(tab_unsorted)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='tri par selection 2')

Y = []


for i in range (min, max, step):
    tab_unsorted = [randint(0,i//2) for _ in range(i)]
    tab_unsorted.sort()
    permute(tab_unsorted, 5, len(tab_unsorted)-5)
    start = time()
    f = select_sort3(tab_unsorted)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='tri par selection 3')



plt.legend()
plt.show()
