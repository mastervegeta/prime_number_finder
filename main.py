import math
n  = int(input("What range do you want to check for primes?: "))
n_squareroot = math.sqrt(n)
list1 = [i for i in range(3,n)[::2]]
list2 = list1
#this utilises the Sieve of Erastosthenes
#to find the primes
for number in lista1:
    if number > n_squareroot:
        break
    for tester in lista1:
        if tester % number == 0 and tester != number:
            list2.remove(tester)
#add the number 2 since it wasn't originally included
list2.insert(0,2)

print(list2)
