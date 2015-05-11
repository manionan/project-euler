def find_largest_root(number):
    for r in range(number -1, 1, -1):
        for e in range(1,101):
            if r**e > number:
                break
            if r**e == number:
                return r
    return number


print find_largest_root(4)
print "----------"
print find_largest_root(36)
print "----------"
print find_largest_root(81)
print find_largest_root(4*5)
    

n_terms = 0
limit = 100
for a in range(2,limit+1):
    rooty = find_largest_root(a)
    #print "a, pow:", a, pow
    if rooty == a:
        n_terms += limit - 1
        continue
    max_pow = rooty**limit
    for b in range(2,limit+1):
        if a**b <= max_pow:
            #print "a**b, max_div_pow:", a**b, max_div_pow
            continue
        n_terms += 1
    
print "n_terms: ", n_terms
