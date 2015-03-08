from problem7 import *

prime_list = list_primes(2,2000000-1)
print "length is: ", len(prime_list)

counter = 1
sum = 0
for prime in prime_list:
    sum += prime
    counter +=1

print "sum is: ", sum
print "counter to: ", counter
