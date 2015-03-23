def count_digits(number):
    count = 0
    while number > 0:
        number = int(number/10)
        count += 1
    return count

suffixes = [1,2,3,4,32,123,43,2123,432,1234,32123,43212,34321,23432,123432]
len_suffixes = []
for suffix in suffixes:
    len_suffixes.append(count_digits(suffix))

print len_suffixes

prefixes = [123432,234321,343212,432123,321234,123432,432123,
            212343,432123,123432,321234,432123,343212,234321,
            123432]

S15 = 0
for suffix in suffixes:
    S15 += suffix

print S15

S10 = 0
for i in range(0,10):
    S10 += suffixes[i]

print S10

sum_prefix_powers = 0
for i in range(0,len(prefixes)):
    sum_prefix_powers += prefixes[i]*(10**len_suffixes[i])

print sum_prefix_powers

sum_10_prefix_powers = 0
for i in range(0,10):
    sum_10_prefix_powers += prefixes[i]*(10**len_suffixes[i])

print sum_10_prefix_powers


#test formulas
print "about to begin" 

n = int(100000000000000/15)
#print n/(2*3)
print "mod: ", n%123454321
n = 2
#n = int(1000/15)
print n

md = 123454321

ratio1 = (1-((10**6))**(n-1) ) / (1-10**6) % md
#ratio1 = (1-(10**6)**(n)) / (1-10**6)
print ratio1

ratio2 = (1-(n-1)*((10**6)**(n-2)) + (n-2)*((10**6)**(n-1)))/((1-10**6)**2) %md
#ratio2 = (1-(n)*((10**6)**(n-1)) + (n-1)*((10**6)**(n)))/((1-10**6)**2)
ratio2 += ratio1 
ratio2 = ratio2 % md
print ratio2

ratio10 = (1-(10**6)**(n)) / (1-10**6)

total = (S15*n) % md
total += (sum_prefix_powers*n*ratio1) % md
total -= (sum_prefix_powers*ratio2) % md
total += S10 %md
total += (sum_10_prefix_powers*ratio10) %md
total = total % md
print total

#print "n%15 = ", 100000000000000 %15
