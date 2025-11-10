from random import randint
from time import time
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(100000)



def permute(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]


# Tri rapide


def partitionner(tab, first, last, pivot):
    permute(tab, pivot, last)
    j = first
    for i in range(first, last):
        if tab[i] <= tab[last]:
            permute(tab, i, j)
            j = j + 1
    permute(tab, last, j)
    return j


def quick_sort(tab, first_index, last_index):
    if first_index < last_index:
        pivot = randint(first_index, last_index)
        pivot = partitionner(tab, first_index, last_index, pivot)
        quick_sort(tab, first_index, pivot -1)
        quick_sort(tab, pivot + 1, last_index)



# Tri par comptage

def count_sort(tab:list):
    max = tab[0]
    min = tab[0]
    for v in tab:
        if v > max:
            max = v
        if v < min:
            min = v
    lcount = [0] * (max - min + 1)
    for v in tab:
        lcount[v-min] +=1
    tab.clear()
    for k, v in enumerate(lcount):
        tab += [k + min] * v
    return tab


min = 1000
max = 50000
step = 1000

X = [x for x in range(min, max, step)]

Y = []

print("debut tri rapide")

for i in range (min, max, step):
    print(i, ":", end=" ", flush=True)
    tab_unsorted = [randint(-i//2,i//2) for _ in range(i)]
    start = time()
    f = quick_sort(tab_unsorted, 0, len(tab_unsorted)-1)
    stop = time()
    Y.append(stop - start)
    for i in range(5):
        print(tab_unsorted[i], end=" ")
    for i in range(len(tab_unsorted) -5, len(tab_unsorted)):
        print(tab_unsorted[i], end=" ")
    print(" ")

plt.plot(X,Y,label='tri rapide')
plt.legend()
Y = []

print("debut tri par comptage")

for i in range (min, max, step):
    print(i, ":", end=" ", flush=True)
    tab_unsorted = [randint(-i//2, i//2) for _ in range(i)]
    start = time()
    f = count_sort(tab_unsorted)
    stop = time()
    Y.append(stop - start)
    for i in range(5):
        print(tab_unsorted[i], end=" ")
    for i in range(len(tab_unsorted) -5, len(tab_unsorted)):
        print(tab_unsorted[i], end=" ")
    print(" ")


plt.plot(X,Y,label='tri par comptage')
plt.legend()
plt.show()
