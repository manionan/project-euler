n = 4

ways = 0
for i in range(0,n):
    for j in range(i,n):
        ways += 1
        

print "ways for 2: ", ways


ways = 0

for i in range(0,n):
    for j in range(i,n):
        for k in range(j,n):
            ways+=1

print "ways for 3: ", ways

ways = 0

for i in range(0,n):
    for j in range(i,n):
        for k in range(j,n):
            for l in range(k,n):
                ways+=1

print "ways for 4: ", ways
