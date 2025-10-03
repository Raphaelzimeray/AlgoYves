#

def is_prime_it(num):
    if num%2 == 0 and num !=2:
        return False
    for i in range(2,num//2):
        if num%i == 0:
            return False
    return True



for i in range(25):
    print(i, "Premier", is_prime_it(i))

# afficher les n premiers nombres premiers
#

def get_prime_numbers(num):
    prime_numbers = []
    i = 0
    while len(prime_numbers) < num:
        if is_prime_it(i) == True:
            prime_numbers.append(i)
        i +=1
    return prime_numbers


for i in range(10):
    print(i, get_prime_numbers(i))
