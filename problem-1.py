sum = 0
m3 = 3
while m3 < 1000:
    sum += m3
    m3 += 3
    
ii = 1
m5 = 5
while m5 < 1000:
    if ii%3 !=0: sum += m5
    m5 += 5
    ii += 1

print "sum is: ", sum
