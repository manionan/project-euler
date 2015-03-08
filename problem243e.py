        
from problem7 import *    
primes = list_primes(2,100000)


def find_incl_primes(number):
    result = []
    for p in primes:

        if p>number: break
        if number == 1: break
        if number % p == 0:
            number /= p
            result.append(p)
            while number %p == 0:
                number /=p

    return result



    #if 94744*n_res < (d-1)*15499:
import math

def find_smallest(max):
   
    for d in range(2,max):
        if d%1000==0:
            print "d = ", d
        incl_primes = find_incl_primes(d)
        n_res = d
        n_div = 1
        for p in incl_primes:
            n_res *= (p-1)
            n_div *= p
        n_res /= n_div
        #n_res = d - math.sqrt(d)
        if 94744*n_res < (d-1)*15499:
        #if 10*n_res < (d-1)*4:
            print "found smallest d: ", d
            return
        
        

find_smallest(10000000)

print "done"


#print incl_primes(70)

