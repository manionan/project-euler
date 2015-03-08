from problem7 import *
primes = list_primes(2,1000)

def is_coprime(m,n):
    a = m**2 + n**2
    b = 2*m*n
    c = m**2 - n**2
    for p in primes:
        if ( (a%p == 0 and b%p ==0) or
             (a%p == 0 and c%p ==0) or
             (b%p == 0 and c%p ==0) ):
            return False
    return True

def find_max_triangles(perimeter_max):
    max_at_any = 0
    P_at_max = 0
    for P in range(1,perimeter_max+1):
        n_at_P = 0
        for n in range(1,25):
            for m in range(n+1,25):
                if is_coprime(m,n) == False:
                    continue
                p = 2*m**2 + 2*m*n
                if P % p == 0:
                    if P==120:
                        print "p fits in P: ", p, P
                        print "     with a, b, c: ", m**2 + n**2, 2*m*n, m**2 - n**2
                    n_at_P += 1

        if n_at_P > max_at_any:
            max_at_any = n_at_P
            P_at_max = P
            print "candidate max () at (): ", max_at_any, P
    return P_at_max

max = find_max_triangles(1000)
print "found max at P = ", max




