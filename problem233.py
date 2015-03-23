import math

print int(-1.5), int(1.5)

def find_points_small(N):
    if N %2 != 0:
        print "Not ready for odd N yet!"
        return None
    ranger = int(math.sqrt(2)*N/2.0)
    
    count = 0
    for x in range(1, N/2+1):
        float_ver = math.sqrt(( ( float(N) )**2 )/2.0  - ( float(x) )**2 )
        if (  float_ver == int(float_ver) ) :
            count += 1

    count *= 8
    count -= 4

    return count




from problem7 import *

first_primes = list_primes(2,1000)

def list_factors(N):
    factors = ""
    for p in first_primes:
        power = 1
        if N % p == 0:
            factors += str(p)
            N /= p
            while N % p == 0:
                N /= p
                power +=1
            factors += "(" + str(power) + ") "

    return factors
            

#print "pre test"
#for i in range(10000,20000,2):
#    points = find_points_small(i)
#    if points == 36:
#        print i, list_factors(i)
#print "end pre test"

primes = list_primes(3,4366864)

shrt_limit = 139230
shorter_primes = list_primes(3,shrt_limit)

p1_primes = []
p3_primes = []

for p in primes:
    if (p-1) % 4 == 0:
        p1_primes.append(p)
    elif (p-3) % 4 == 0:
        p3_primes.append(p)
    else:
        print "prime doesn't fit!"


p1_shorter = []
for p in shorter_primes:
    if (p-1) % 4 == 0:
        p1_shorter.append(p)

#print p1_primes
#print p3_primes

print len(p1_primes)
print len(p3_primes)
print len(shorter_primes)

#print p1_shorter

limit = 10**11
steps = []
##(2+1)*(4+1)*(6+1) = 105 check
base = 2
for q1 in p1_primes:
    base = 2*(q1**3)
    if base > limit: break

    for q2 in p1_primes:
        if q2 == q1: continue
        base = 2*(q1**3)*(q2**2)
        if base > limit: continue

        for q3 in p1_primes:
            if q3 == q2 or q3 == q1: continue
            base = 2*(q1**3)*(q2**2)*(q3)
            if base > limit: continue
            
            steps.append(base)

#(6+1)*(14+1) = 105 check
base = 2
for q1 in p1_primes:
    base = 2*(q1**7)
    if base > limit: break

    for q2 in p1_primes:
        if q2 == q1: continue
        base = 2*(q1**7)*(q2**3)
        if base > limit: continue
        if base == 16900:
            print "found bad actor in loop2, q1,q2: ", q1,q2
        steps.append(base)


##(4+1)*(20+1) = 105 check
base = 2
for q1 in p1_primes:
    base = 2*(q1**10)
    if base > limit: break

    for q2 in p1_primes:
        if q2 == q1: continue
        base = 2*(q1**10)*(q2**2)
        if base > limit: continue
        if base == 16900:
            print "found bad actor in loop3, q1,q2: ", q1,q2
        steps.append(base)
            

##

#print "steps: ", steps



print "n_steps: ", len(steps)

steps_sort = sorted(steps)
print "done sorting"

print "first element: ", steps_sort[0]

#print "test: ", find_points_small(718250)
#print "test2: ", find_points_small(2*5*5*5*13*13*17*7*11)
#print "test3: ", find_points_small(2*(13**4))
#print "test4: ", find_points_small(2*13*(5**2))
#print "test5: ", find_points_small(2*5*(13**2))
#print "test6: ", find_points_small(2*(5**7))
#print "test7: ", find_points_small(2*(5**7)*(13**3))
print "test8: ", find_points_small(718250)
summy = 0
for i in range(1,shrt_limit):
    found = False
    if i % 10000 == 0:
        print i
    for p in p1_shorter:
        if i % p == 0:
            found = True
            break
        if p > i:
            break
    if found == True:
        continue
    n_steps = 0
    for s in steps_sort:
        if i*s > limit:
            #print "limit!"
            break
        #print find_points_small(i*s)
        summy += i*s
        n_steps += 1
    if n_steps == 0:
        print "hit limit at", i
        break

print summy
        
