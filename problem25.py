#based on moving the 10's digit up the line
n = {}
n_prime = {}
n_dprime = {}

for i in range(0, 1000):
    n[i] = 0
    n_prime[i] = 0
    n_dprime[i] = 0

n[0] = 3 #start with 3
n_prime[0] = 5 #and next term is 5

term = 5
while n_dprime[999] == 0: #until reach 1000 digits
    
    n_dprime[0] = (n_prime[0] + n[0]) % 10
    carry = int((n_prime[0] + n[0])/10)

    for i in range(1, 1000):
        n_dprime[i] = (n_prime[i] + n[i] + carry) % 10
        carry = int( (n_prime[i] + n[i] + carry) / 10 )

    for i in range(0, 1000):
        n[i] = n_prime[i]
        n_prime[i] = n_dprime[i]

    term += 1

print "final term: ", term
