        
from problem7 import *    
primes = list_primes(2,30)


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

def check_number(d):
   
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
        print "found smallest d, n_res: ", d, n_res
        return d
    else:
        #print "res not small enough: d, n_res", d, n_res
        return -1
        
        
        
check_number(2*3*5*7*11*13*17*19*23*29)
check_number(2*3*5*7*11*13*17*19*23*5) #replace 29   
check_number(2*3*5*7*11*13*17*5*23) #replace 19

print "powers:"
big_number = 2*3*5*7*11*13*17*19*23*29

def get_powers_needed(p,big_number):
    n = 1
    powered = p
    while powered < big_number:
        powered *=p
        n += 1
    return n

print "powers of 2 needed: ", get_powers_needed(2,big_number)
print "powers of 3 needed: ", get_powers_needed(3,big_number)
print "powers of 5 needed: ", get_powers_needed(5,big_number)
print "powers of 7 needed: ", get_powers_needed(7,big_number)
print "powers of 11 needed: ", get_powers_needed(11,big_number)
print "powers of 13 needed: ", get_powers_needed(13,big_number)
print "powers of 17 needed: ", get_powers_needed(17,big_number)
print "powers of 19 needed: ", get_powers_needed(19,big_number)
print "powers of 23 needed: ", get_powers_needed(23,big_number)
print "powers of 29 needed: ", get_powers_needed(29,big_number)

def find_min():
    big_number = 2*3*5*7*11*13*17*19*23*29
    smallest = big_number
    d = 1
    for i2 in range(0,10):
        d2 = 2**i2
        d = d2
        print "i2: ", i2
        if d > big_number: continue
        
        for i3 in range(0,9):
            d3 = 3**i3
            d = d2*d3
            if d > big_number: continue
            
            
            for i5 in range(0,8):
                d5 = 5**i5
                d = d2*d3*d5
                if d > big_number: continue
                
                
                for i7 in range(0,7):
                    d7 = 7**i7
                    d = d2*d3*d5*d7
                    if d > big_number: continue
                    
                    
                    for i11 in range(0,6):
                        d11 = 11**i11
                        d = d2*d3*d5*d7*d11
                        if d > big_number: continue
                        
                        
                        for i13 in range(0,5):
                            d13 = 13**i13
                            d = d2*d3*d5*d7*d11*d13
                            if d > big_number: continue
                            
                            
                            for i17 in range(0,4):
                                d17 = 17**i17
                                d = d2*d3*d5*d7*d11*d13*d17
                                if d > big_number: continue
                                
                                
                                for i19 in range(0,3):
                                    d19 = 19**i19
                                    d = d2*d3*d5*d7*d11*d13*d17*d19
                                    if d > big_number: continue
                                    
                                    
                                    for i23 in range(0,2):
                                        d23 = 23**i23
                                        d = d2*d3*d5*d7*d11*d13*d17*d19*d23
                                        if d > big_number: continue


                                        for i29 in range(0,2):
                                            d29 = 29**i29
                                            d = d2*d3*d5*d7*d11*d13*d17*d19*d23*d29
                                            if d > big_number: continue
                                            
                                            c = check_number(d)
                                            if c > 0:
                                                if c<smallest:
                                                    smallest = c
                                            
    print "smallest was: ", d
find_min()
print "done"


#print incl_primes(70)

