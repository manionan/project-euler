n_to_test = 10

def find_prime_mult_lt(b,primes):

    for l in range(b,1,-1):
        #print l
        found = True
        for p in primes:
            if l % p == 0:
                found = False
                break
        if found == True:
            return l

    return 0


        
from problem7 import *    
primes = list_primes(3,1000000)

def count_divisors(number,primes_list):
    prime_exp = []
    for prime in primes_list:
        if prime > number:
            print "shouldna used gt prime"
            break
        n_exp = 0
        while number%prime == 0:
            number /= prime
            n_exp += 1
        if n_exp!=0:
            prime_exp.append(n_exp)
    n_divisors = 1
    for e in prime_exp:
        n_divisors *= (1+e)

    return n_divisors

print "count divisors test: ", count_divisors(7,[3,5,7])
#import math

#def ways(n):
#    n_ways = 0
#    n_ways = math.factorial(2*n)/(math.factorial(n)**2) -2
    #else:
    #    n_ways = int( (4.0**n)/math.sqrt(math.pi*n) ) - 2
#    return n_ways

#for i in range(1,15):
#    print "i, ways, 2**n: ", i, ways(i), 2**i



def find_smallest(min,max):
    for d in range(min,max,2):
        
        if d%1000 == 0:
            print "d =", d
        
        incl_primes = []
        for p in primes:
            if p > d: break
            if d % p == 0:
                incl_primes.append(p)
                
        #excl_lt = find_prime_mult_lt(d,incl_primes)
        
        
        n_res = d/2
        for a in range(3,d,2):
            for i in incl_primes:
                if a % i == 0:
                    n_res -=1
                    break
        
        #print "d, n_res: ", d, n_res
        if 94744*n_res < (d-1)*15499:
        #if 10*n_res < (d-1)*4:
            print "smallest denom found!"
            print "n_res, d:", n_res, d
            return
        

find_smallest(216000,1000000)
print 
