from problem7 import *

def count_divisors(number,prime_max):
    primes = list_primes(2,prime_max)
    prime_exp = []
    for prime in primes:
        if prime > number:
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


def find_triangle_with(n_divisors,prime_max):
    n = 1
    this_divisors = 0
    triangle = 0
    while this_divisors < n_divisors:
        triangle = n*(n+1)/2
        this_divisors = count_divisors(triangle,prime_max)
        n+=1

    print triangle, "is triangle number with", this_divisors, "divisors"

find_triangle_with(6,1000)
find_triangle_with(501,1000)
