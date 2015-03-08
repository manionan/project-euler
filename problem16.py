#based on moving the 10's digit up the line
n = {}
n_prime = {}

for i in range(0, 303):
    n[i] = 0
    n_prime[i] = 0
    
n[0] = 2 #start with 2^1

for p in range(0, 999): #add 999 more powers
    
    n_prime[0] = (2*n[0]) % 10
    carry = int(2*n[0]/10)

    for i in range(1, 303):
        n_prime[i] = (2*n[i] + carry) % 10
        carry = int( (carry + 2*n[i]) / 10 )

    for i in range(0, 303):
        n[i] = n_prime[i]

sum = 0
for i in range(0, 303):
    sum += n[i]

print "final sum: ", sum
