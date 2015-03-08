prev_2 = 1
prev_1 = 2
current = 3
sum = 2

while current < 4000000:
    prev_2 = prev_1
    prev_1 = current
    current = prev_2 + prev_1
    if current > 4000000:
        break
    elif current % 2 == 0: 
        sum += current

print "sum is: ", sum
print "current is: ", current
