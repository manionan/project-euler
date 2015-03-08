n_to_test = 1000000

def gcd(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
        elif a == b:
            return b
        else: 
            print "problem 1 with algo"
            return 0

    if a == 0 and b > 0:
        return b
    elif b == 0 and a > 0:
        return a
    else: 
        print "problem 2 with algo"
        return 0
    
from problem7 import *    
primes = list_primes(2,10000)

primes_reverse = sorted(primes,reverse=True)
#print primes_reverse

def lcd(a,b):
    for p in primes:
        if p > a or p > b:
            break
        if a%p == 0 and b%p==0:
            return p
    return 1

def gcd2(a,b):
    for p in primes_reverse:
        if a%p == 0 and b%p == 0:
            return p
            print "found p of: ", p
    return 1
    

smallest_found = False
for d in range(2,n_to_test):
    if d%1000==0:
        print "d = ", d
    n_res = d-1
    for n in range(1,d):
        if (d-n < d/2):
            if lcd(d,n)>1:
                n_res -=1
        else:
            if gcd2(d,n)>1:
                n_res -=1

        #if gcd(d,n)>1:
        #    n_res -=1
    if 94744*n_res < (d-1)*15499:
    #if 10*n_res < (d-1)*4:
        print "smallest denom found!"
        print "n_res, d:", n_res, d
        smallest_found = True
        break
    
        
