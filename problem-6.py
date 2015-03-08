def difference(limit):
    diff = 0
    for i in range (1, limit+1):
        diff -= i**2
        for j in range (1, limit+1):
            diff += i*j
            
    print "difference is: ", diff

difference(10)
difference(100)
