###############

def flip(num,denom):

    number = [denom,num]
    return number

###############

def sum_digits(n):
    if n==0: return 0
    sum = 0
    while n > 0: 
        sum += n % 10
        n /= 10
    return sum

###############

def make_sum_frac(a, num_b, denom_b):

    number = [0,0]
    number[0] = a*denom_b + num_b
    number[1] = denom_b

    return number

###############

from problem7 import *
primes = list_primes(2,10000)

def reduce_frac(num,denom):
    number = [0,0]

    for p in primes:
        if p > num:
            break
        if num % p == 0 and denom % p == 0:
            num /= p
            denom /= p

    number[0] = num
    number[1] = denom
    
    return number

################

def find_100th_convergent():
    
    terms = []
    for i in range(1,34):
        terms.append(1)
        terms.append(2*i)
        terms.append(1)

    fraction = make_sum_frac(terms[97],1,terms[98])
    fraction = reduce_frac(fraction[0],fraction[1])

    for i in range(96,-1,-1):
        fraction = flip(fraction[0],fraction[1])
        fraction = make_sum_frac(terms[i],fraction[0],fraction[1])
        fraction = reduce_frac(fraction[0],fraction[1])

    fraction = flip(fraction[0],fraction[1])
    fraction = make_sum_frac(2,fraction[0],fraction[1])
    fraction = reduce_frac(fraction[0],fraction[1])

    print fraction

    print sum_digits(fraction[0])

find_100th_convergent()
        
