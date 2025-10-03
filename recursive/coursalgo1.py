from random import randint

print("bonjour")

def recursive1(n):
    if n == 0:
        print("la fonction s'arrete", n)
    else:
        print("on est dans la récursivité", n)
        recursive1(n-2)


def recursive2(n):
    if n <= 0:
        print("la fonction s'arrete", n)
    else:
        recursive2(n-1)
        print("on est dans la récursivité", n)


def sum1(n):
    if n == 0:
        return 0
    else:
        return n + sum1(n-1)


def factoriel(n):
    if n <= 1:
        return 1
    else:
        return n * factoriel(n-1)


# recursive1(11)

for i in range(11):
    print("factoriel de", i, factoriel(i))



def ispalindrome(txt):
    if len(txt) <= 1:
        return True
    else:
        return txt[0] == txt[-1] and ispalindrome(txt[1:-1])


mots = ["coucou", "ananas", "radar", "kayak"]

for mot in mots:
    if ispalindrome(mot):
        print(mot, "est un palindrome")
    else:
        print(mot, "n'est pas un palindrome")



#print years rec

def printyearsrec(year1, year2):
    if year2 < year1:
        print("c'est fini")
    else:
        print("voici l'année", year1)
        printyearsrec(year1 + 1, year2)


print("test de print years rec", printyearsrec(2010, 2020))


# power rec

def power_rec(n, p):
    if p == 1:
        return n
    # else:
    return n * power_rec(n, p -1)

    # sur 2^4 => return 2 * power_rec(2, 3) c'est à dire
    #         => return 2 * (2 * power_rec(2,2))
    #         => return 2 * 2 * (2 *  power_rec(2,1))
    #         => return 2 * 2 * 2 * (2)


for p in range (1, 11):
    print("3 puissance ", p,":", power_rec(3, p))


# number of digits in number

# 12870

def number_of_digits_rec(n):
    if n < 1:
        return 0
    else:
        return 1 + number_of_digits_rec(n/10)

    # 12870 => 1 + nod(1276)
    # 12870 => 1 + (1 + nod(127,6))
    # 12870 => 1 + 1 + (1 + nod(12,76))
    # 12870 => 1 + 1 + 1 + (1 + nod(1,276))
    # 12870 => 1 + 1 + 1 + 1 + (1 + nod(0,1276))
    # 12870 => 1 + 1 + 1 + 1 + 1 + (0) => 5

print("il y a ", number_of_digits_rec(1287089893), " chiffres dans 12870")

for _ in range(10):
    n = randint(1, 10**randint(1, 8))
    n = randint(1, 10**8)
    print("il y a ", number_of_digits_rec(n), " chiffres dans ", n)


# 14565

def sum_of_digits_rec(n):
    if n < 10:
        return n
    else:
        return n%10 + sum_of_digits_rec(n//10)

    #14565 => 14565%10 + sod(14565 // 10)
    #14565 => 5 + sod(1456)
    #14565 => 5 + 6 + sod(145)
    #14565 => 5 + 6 + 5 + sod(14)
    #14565 => 5 + 6 + 5 + 4 + sod(1)
    #14565 => 5 + 6 + 5 + 4 + 1 => 21


print("test de sum of digits", sum_of_digits_rec(14565))
