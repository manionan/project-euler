from problem7 import *

def count_digits(n):
    n_digits = 0

    while n > 0:
        n /= 10
        n_digits += 1

    return n_digits

def remove_left(number,n):
    n_digits = count_digits(number)
    rem = number / 10**(n_digits - n)
    rem *= 10**(n_digits - n)
    new = number - rem
    return new

def remove_right(number,n):
    new = number / 10**n
    return new

primes = list_primes(2,1000000)

rev_primes = reversed(primes)

cool = []
test_primes = [3797]
for r in rev_primes:

    n_digits = count_digits(r)
    candidate = []

    for d in range(1,n_digits):
        candidate.append(remove_left(r,d))
        candidate.append(remove_right(r,d))

    
    #candidate.sort()

    all_prime = True
    for can in candidate:

        can_prime = False

        for p in primes:
            if p > can:
                break
            if p == can:
                can_prime = True
                break
        
        if can_prime == False:
            all_prime = False
            break
       
    if all_prime == True:
        cool.append(r)

print cool

total = 0
for i in range(0,11):
    total += cool[i]

print "total sum:", total
