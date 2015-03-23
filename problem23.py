def get_sum_div(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum

print get_sum_div(28)

abundant = []

limit = 28123

for i in range(2,limit+1):
    if i % 1000 == 0:
        print i
    if get_sum_div(i) > i:
        abundant.append(i)

print "length:", len(abundant)

sum = limit*(limit+1)/2

hit = {}
for i in range(1,limit+1):
    hit[i] = False

for i in abundant:
    for j in abundant:
        if j < i: 
            continue
        if i+j > limit:
            continue
        if hit[i+j] == False: 
            sum -= i+j
            hit[i+j] = True

print "final sum:", sum
