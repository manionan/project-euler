#based on moving the 10's digit up the line
n = {}
n_prime = {}

for i in range(0, 160):
    n[i] = 0
    n_prime[i] = 0
    
n[0] = 1 #start with 1

for t in range(2, 101): #mult 99 more terms
    
    n_prime[0] = (t*n[0]) % 10
    carry = int(t*n[0]/10)

    for i in range(1, 160):
        n_prime[i] = (t*n[i] + carry) % 10
        carry = int( (carry + t*n[i]) / 10 )

    for i in range(0, 160):
        n[i] = n_prime[i]

sum = 0
for i in range(0, 160):
    sum += n[i]

print "final sum: ", sum
