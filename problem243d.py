        
from problem7 import *    
primes = list_primes(100,200)

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

def find_incl_primes(number):
    result = []
    for p in primes:
        if p>number: break
        if number % p == 0:
            result.append(p)
    return result

def com_primes(number1,number2):
    result = []
    for p in primes:
        if p>number1 or p>number2: break
        if number1 %p ==0 and number2 %p ==0:
            result.append(p)
    return result

def run_check(d,incl_primes):

    n_res = d-1
    for a in range(2,d):
        for i in incl_primes:
            if a % i == 0:
                n_res -=1
                break

    #if 94744*n_res < (d-1)*15499:
    if 10*n_res < (d-1)*4:
        return n_res
    else: 
        return 0

def find_smallest():
    smallest = 1
    current =1
    minimum = 500000
    for a in range(0,len(primes)):
        p_a = primes[a]
        if p_a > minimum:
            current = run_check(p_a,[p_a])
            if current > 0:
                print "found n_res, d: ", current, p_a
            
        for b in range(a+1,len(primes)):
            p_b = primes[b]
            if p_a*p_b > minimum:
                current = run_check(p_a*p_b,[p_a,p_b])
                if current > 0:
                    print "found n_res, d: ", current, p_a*p_b
        
            for c in range(b+1,len(primes)):
                p_c = primes[c]
                if p_a*p_b*p_c > minimum:
                    current = run_check(p_a*p_b*p_c,[p_a,p_b,p_c])
                    if current > 0:
                        print "found n_res, d: ", current, p_a*p_b*p_c

                #for d in range(c,len(primes)):
                #    p_d = primes[d]
                #    if p_a*p_b*p_c*p_d > minimum:
                #        current = run_check(p_a*p_b*p_c*p_d,[p_a,p_b,p_c,p_d])
                #        if current > 0:
                #            print "found n_res, d: ", current, p_a*p_b*p_c*p_d
   
        

find_smallest()

print "done"


#print incl_primes(70)

print 15499.0/94744.0
