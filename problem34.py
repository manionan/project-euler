

def factorial_pre(n):
    if n == 0:
        return 1
    fact = 1
    while n>0:
        fact *= n
        n -= 1
    return fact

#precompute factorials
factorial = {}
for i in range(0,10):
    factorial[i] = factorial_pre(i)

def find_max_terms():
    number = 9
    fact_9 = factorial[9]
    sum_facts = fact_9
    n_tried = 1
    while number < sum_facts:
        number += 9*(10**(n_tried))
        sum_facts += fact_9
        n_tried += 1
    print "max terms = ", n_tried

find_max_terms()

def find_numbers():
    numbers = []
    for i in range(3,9999999):
        sum = 0
        n_length = 0
        temp_number = i
        while temp_number > 0:
            temp_number = int(temp_number/10)
            n_length += 1
        for t in range(0,n_length):
            sum += factorial[int(i/(10**t)) % 10]
        if sum == i:
            numbers.append(i)

    return numbers

n_satisfy = find_numbers()

sum = 0
for n in n_satisfy:
    sum += n

print "final sum is: ", sum
print n_satisfy

print factorial[1] + factorial[4] + factorial[5] + factorial[]
