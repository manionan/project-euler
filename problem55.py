from problem4 import *

n_lych = 9999  
for i in range(1,10000):
    n = 1
    resultant = i
    while n < 50:
        resultant = resultant + reverse_integer(resultant)
        digits = digit_count(resultant)
        n_to_check = digits/2
        first = get_first(resultant,n_to_check)
        last = get_last_reversed(resultant,n_to_check)
        if first == last:
            n_lych -= 1
            break
        n += 1


print "n_lych =", n_lych
