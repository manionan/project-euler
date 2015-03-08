from problem7 import*
primes = list_primes(2,100000)

print "listed primes"

is_prime = {}
for i in range(2,100000):
    is_prime[i] = False

for p in primes:
    is_prime[p] = True

print "prime bool set"

is_comb = {}
for i in range(1,100000):
    is_comb[i] = False

print "comb bool initialized"

for p in primes:
    for i in range(1,3163):
        comb = p + 2*(i**2)
        if comb >= 100000:
            continue
        is_comb[comb] = True

print "comb bool set"

#now check odd non-primes against composites
for i in range(3,100000,2):
    if is_prime[i]:
        continue
    if is_comb[i] == False:
        print "found first non-comb composite: ", i
        break

