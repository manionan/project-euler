#prime sieve calls

def list_primes(min, max):
    if min<2 or max<= min:
        print "list_primes: invalid max or min"
        return None

    is_prime = {} #dict, prime->is_prime
    for i in range(min,max+1):
        is_prime[i] = True

    candidate = 2
    #case for 2 first
    while candidate <= max:
        candidate += 2
        if candidate >= min and candidate <= max: is_prime[candidate] = False

    #case for other odd numbers only (cut time in half)
    for m in range(3,max+1,2):
        candidate = m
        while candidate <= max:
            candidate += m
            if candidate >= min and candidate <= max: is_prime[candidate] = False

    prime_list = [] #list of primes
    for i in is_prime.keys():
        if is_prime[i] == True:
            prime_list.append(i)

    return prime_list


def get_nth_prime(n,max):
    prime_list = list_primes(2,max)
    if len(prime_list) < n:
        print "get_nth_prime: max to small to get nth prime"
        return None
    else:
        return prime_list[n-1]

#print get_nth_prime(10001,1000001)
