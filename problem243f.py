        
from problem7 import *    
primes = list_primes(2,1000000)




    #if 94744*n_res < (d-1)*15499:

def find_smallest(max):
    d = 1
    for f in range(0,max):
        d *= primes[f] 
        if f%100==0:
            print "d = ", d
        n_res = d
        n_div = 1
        for i in range(0,f+1):
            p = primes[i]
            n_res *= (p-1)
            n_div *= p
        n_res /= n_div
        #n_res = d - math.sqrt(d)
        if 94744*n_res < (d-1)*15499:
        #if 10*n_res < (d-1)*4:
            print "found smallest d, n_res): ", d, n_res
            print "f was: ", f
            return
        
        

find_smallest(1000)

print "done"


#print incl_primes(70)

