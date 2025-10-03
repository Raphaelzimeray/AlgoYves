# tableau trié par ordre croissant, la question c'est est ce que le nombre "n" est dans ce tableau

from random import randint

list_test = [randint(0,100) for _ in range(50)]

print (list_test)

list_test.sort()

print(list_test)


def is_intab(tab, num):
    i = 0
    while tab[i] < num:
        i+=1
    return tab[i] == num


for i in range(10, 20):
    print(i, ":", is_intab(list_test, i))
