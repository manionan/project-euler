import math


def get_period(squared):

    num = 1
    denom = - int(math.sqrt(squared))
    num_pre = 1

    in_sqrt = math.sqrt(squared)
    #print "in sqrt:", in_sqrt
    period = 0

    n = 0
    while 0 == 0:
        n +=1
        #print "num, denom: ", num, denom
        period += 1

        num_prime = -denom
        num_pre = num

        denom_prime = (squared - denom**2)

        
              
        if denom_prime == 1:
            break

        if denom_prime >= num_pre:
            if denom_prime % num_pre != 0:
                print "PROBLEM!!!!"
            denom_prime /= num_pre
            num_pre = 1

        if denom_prime == 1:
            break

        
        num_prime = num_prime - int( (in_sqrt + float(num_prime)) / float(denom_prime) )*denom_prime


        num = denom_prime
        denom = num_prime
    return period



#print "PERIOD 23:", get_period(23)
#print "PERIOD 2:", get_period(2)
#print "PERIOD 3:", get_period(3)
#print "PERIOD 5:", get_period(5)
#print "PERIOD 6:", get_period(6)
#print "PERIOD 7:", get_period(7)
#print "PERIOD 8:", get_period(8)
#print "PERIOD 10:", get_period(10)
#print "PERIOD 11:", get_period(11)
#print "PERIOD 12:", get_period(12)
#print "PERIOD 13:", get_period(13)

is_square = {}

for i in range(2,10001):
    is_square[i] = False

for i in range(2,101):
    is_square[i**2] = True

n_odd = 0
for i in range(2,10001):

    if is_square[i] ==  True:
        #print i, "PERIOD", 0
        continue
    
    period = get_period(i)
    if period % 2 != 0:
        n_odd +=1
    #print i, "PERIOD", period


print "n_odd =", n_odd
