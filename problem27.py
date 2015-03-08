from problem7 import *

primes_b = list_primes(2,1001)

primes = list_primes(2,50000)
print "got primes list." 

max_n = 0
product = 0
for a in range(-999,1000):
    print " a = ", a
    for b in primes_b:
        n = 1
        while n < 81:
            formula = (n**2 + a*n + b)
            if formula < 2: break
            found = False
            for p in primes:
                if (formula == p):
                    n+=1
                    found = True
                    break
            if found == False: break
            if n>max_n:
                max_n = n
                product = a*b
                    

print "found max n of: ", max_n, "with product: ", product

