import math
#start at n = 4
n = 4
running_sum = 7
result = 8

for i in range(0,10):
    running_sum += result
    print "running sum: ", running_sum
    result = (running_sum + 1)*math.floor(n/2.0)
    n += 1
    print "n=", n, "result: ", result
