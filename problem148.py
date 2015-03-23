print 1000000001 % 7**

print 1000000001 /7
print 1000000001 /7/7
print 1000000001 /7/7/7
print 1000000001 /7/7/7/7
print 1000000001 /7/7/7/7/7
print 1000000001 /7/7/7/7/7/7
print 1000000001 /7/7/7/7/7/7/7
print 1000000001 /7/7/7/7/7/7/7/7
print 1000000001 /7/7/7/7/7/7/7/7/7
print 1000000000 /7/7/7/7/7/7/7/7/7/7

n_rows = 1000000000
limit = (n_rows + 1)/ 7 
print "limit:", limit

i = 0
n_divisie = 0
while i < limit + 1:
    if i % 10000000 == 0:
        print i
    n_divisie += 21*i
    i+=1

print "first pass done"

limit = (n_rows + 1)/7/7
while i < limit + 1:
    if i % 500000:
        print i
    n_divisie += (49*25-21*21)*i

n_total = n_rows*(n_rows+1)/2 
n_not_divisie = n_total - n_divisie

print "total, divis: ", n_total, ", ", n_divisie
print n_not_divisie
