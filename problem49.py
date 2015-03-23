from problem7 import *

def list_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = int(number/10)

    digits = sorted(digits)
    return digits

#print list_digits(1234)
#print list_digits(2233)

primes = list_primes(1000,9999)

#print len(primes)


ps_digits = {}

for p in primes:
    ps_digits[p] = list_digits(p)
    

has_friends = {}

for p in primes:
    has_friends[p] = False

friends = {}

for p in primes:
    n_friends = 0
    ps_friends = []
    for q in primes:
        if q <= p: continue
        all_four = True
        for i in range(0,4):
            if ps_digits[p][i] != ps_digits[q][i]:
                all_four = False
        if all_four == True:
            ps_friends.append(q)
            n_friends += 1
           
                
    if n_friends >= 2:
        has_friends[p] = True
        friends[p] = ps_friends

#print friends
print len(friends)
for key in friends.keys():
    fs = friends[key]
    
    if len(fs) == 2:
        if fs[0] - key == fs[1] - fs[0]:
            print "found one!"
            print key, fs
            
