#pascal triangle mod 7
for i in range(1,12):
    print i, 7**i, (1000000001 % (7**i))/float(7**i) 
