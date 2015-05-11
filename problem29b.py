distinct_pows = {}
limit = 100
for a in range(2,limit + 1):
    for b in range(2,limit + 1):
        distinct_pows[a**b] = True

count = 0
for key in distinct_pows.keys():
    count +=1

print "final count:", count
