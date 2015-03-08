def find_max_terms():
    number = 9
    sum_powers = 9**5
    n_tried = 1
    while number < sum_powers:
        number += 9*(10**(n_tried))
        sum_powers += 9**5
        n_tried += 1

    print "max terms = ", n_tried

find_max_terms()


def find_numbers():
    numbers = []
    for i in range(32,999999):
        sum = 0
        for t in range(0,6):
            sum += (int(i/(10**t)) % 10)**5
        if sum == i:
            numbers.append(i)

    return numbers

n_satisfy = find_numbers()

sum = 0
for n in n_satisfy:
    sum += n

print "final sum is: ", sum
print n_satisfy

print 4**5 + 1**5 + 5**5
print 4**5 + 1**5 + 5**5 + 1**5
print 1**5 + 9**5 + 4**5 + 9**5 + 7**5 + 9**5
