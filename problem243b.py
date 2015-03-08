n_to_test = 500000
minimum_to_test = 10000

import math

def ways(n):
    n_ways = 0
    n_ways = math.factorial(2*n)/(math.factorial(n)**2) -2
    #else:
    #    n_ways = int( (4.0**n)/math.sqrt(math.pi*n) ) - 2
    return n_ways

from problem7 import *    
primes = list_primes(2,1000000)

    
smallest_found = False
n_primes = 0
d = 1
for f in range(0,min(n_to_test,len(primes))):
    if f%100==0:
        print "f = ", f
        print "d = ", d
    d*=primes[f]
    #if(d<10000): continue
    n_elim = ways(f+1)

    n_res = (d-1) - n_elim
    
    if 94744*n_res < (d-1)*15499:
    #if 10*n_res < (d-1)*4:
        print "smallest denom found!"
        print "n_res, d:", n_res, d
        smallest_found = True
        break
        
