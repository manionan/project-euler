def find_triplet_prod():
    product = 0
    for a in range(1,334):
        for b in range(1,667-a):
            c = 1000 - a - b
            #print "a^2 + b^2: ", a**2 + b**2
            if (a**2 + b**2 == c**2):
               product = a*b*c
               print "a, b, c: ", a, b, c
               break
    return product
            

print find_triplet_prod()
