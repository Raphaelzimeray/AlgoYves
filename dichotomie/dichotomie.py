# tableau trié par ordre croissant, la question c'est est ce que le nombre "n" est dans ce tableau

from random import randint
from matplotlib import pyplot as plt
from time import time

def is_intab(tab, num):
    i = 0
    while tab[i] < num:
        i+=1
    return tab[i] == num


# Version itérative

def is_intab_dichotomie(tab, num):
    begin = 0
    end = len(tab) - 1
    middle = (begin + end) // 2
    while tab[middle] != num and begin < end:
        if tab[middle] > num:
            end = middle - 1
        else:
            begin = middle + 1
        middle = (begin + end) // 2
    if tab[middle] == num:
        return middle
    else:
        return -1


# Version récursive

def is_in_tab_dichotomie_rec_intern(tab, num, begin, end):
    middle = (begin + end) // 2
    if tab[middle] == num:
        return middle
    if begin > end and tab[middle] != num:
        return -1
    if tab[middle] > num:
        return is_in_tab_dichotomie_rec_intern(tab, num, begin, middle -1)
    else:
        return is_in_tab_dichotomie_rec_intern(tab, num, middle + 1, end)



def is_in_tab_dichotomie_rec(tab, num):

    return is_in_tab_dichotomie_rec_intern(tab, num, 0, len(tab)-1)



min = 100
max = 100000
step = 1000

X = [x for x in range(min, max, step)]

Y = []

# for i in range (min, max, 100):
#     print(i, end=" ")
#     list_test = [randint(0,2*i) for _ in range(i)]
#     list_test.sort()
#     start = time()
#     res = is_intab(list_test, i)
#     stop = time()
#     Y.append(stop - start)

# plt.plot(X,Y,label='fonction de tri basique')

# vider la liste Y
Y.clear()

for i in range (min, max, step):
    list_test = [randint(0,2*i) for _ in range(i)]
    list_test.sort()
    start = time()
    res = is_intab_dichotomie(list_test, i)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='fonction de tri dichotomique')

#Vider la liste
Y.clear()


for i in range (min, max, step):
    list_test = [randint(0,2*i) for _ in range(i)]
    list_test.sort()
    start = time()
    res = is_in_tab_dichotomie_rec(list_test, i)
    stop = time()
    Y.append(stop - start)

plt.plot(X,Y,label='fonction de tri dichotomique recursif')

plt.legend()
plt.show()
