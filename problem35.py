def permutations(number):
    perms = []

    n_dig = -1
    temp_num = number
    while temp_num > 0:
        temp_num /= 10
        n_dig += 1
    
    for i in range(0,n_dig):
        perms.append( (number%(10**(i+1)))*(10**(n_dig-i)) + number/(10**(i+1)) )
    return perms

print "perms 12045: ", permutations(12045)

from problem7 import *
primes = list_primes(2,10000000)

print "got primes"

is_prime = {}
for i in range(0,10000000):
    is_prime[i] = False

print "inited dict"

for p in primes:
    is_prime[p] = True
print "set prime bools"

n_circ = 0
for p in primes:
    is_circ = True
    perms = permutations(p)
    for i in perms :
        if is_prime[i] == False:
            is_circ = False
    if is_circ:
        n_circ += 1

print "n_circ = ", n_circ

    
