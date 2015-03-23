from problem7 import *

primes = list_primes(2,1000)

def reduceF(num,denom):
    for p in primes:
        if num == p or denom == p:
            break
        while num % p == 0 and denom % p == 0:
            num /= p
            denom /= p

    fraction = [num,denom]
    return fraction

import math

tot = 10**12

one_over_sqrt2 = 1.0/math.sqrt(2.0)

old_root_0 = 2
old_root_1 = 3
new_root_0 = old_root_0
new_root_1 = old_root_1


i = 0
while i < 5:
    
    if i % 1 == 0:
        print i
        print "num / denom: ", new_root_0, "/", new_root_1
    #mult = int(tot/new_root_1) + 1
    mult = 1
    
    root_mid_0 = new_root_0*mult
    root_mid_1 = new_root_1*mult

    root_high_0 = root_mid_0 + 1
    root_high_1 = root_mid_1 + 1

    root_low_0 = root_mid_0 - 1
    root_low_1 = root_mid_1 - 1

    if root_high_0*root_mid_0 == 2*root_high_1*root_mid_1:
        print "FOUND at Nb =", root_high_0
        print "Ntot =", root_high_1

    elif root_mid_0*root_low_0 == 2*root_mid_1*root_low_1:
        print "FOUND at Nb =", root_mid_0
        print "Ntot =", root_mid_1

    new_root_0 = 2*old_root_0*old_root_1
    new_root_1 = old_root_1**2 + 2*(old_root_0**2)

    for p in primes:
        if new_root_0 == p or new_root_1 == p:
            break
        while new_root_0 % p == 0 and new_root_1 % p == 0:
            new_root_0 /= p
            new_root_1 /= p

    #print "num", 2*old_root_0*old_root_1
    #print "denom", old_root_1**2 + 2*(old_root_0**2)
    old_root_0 = new_root_0
    old_root_1 = new_root_1

    i += 1
