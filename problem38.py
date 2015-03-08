#in particular, import digit_repeat_or_contain_zero(number) and
#count_digits(number)
from problem32 import *


largest = 123456788

digit_to_terms = {}
digit_to_terms[1] = 9
digit_to_terms[2] = 4
digit_to_terms[3] = 3
digit_to_terms[4] = 2

for i in range(1,9999):
    number = ''
    for t in range(1,digit_to_terms[count_digits(i)] + 1):
        number += str(i*t)
    if digit_repeat_or_contain_zero(int(number)): continue
    if int(number) > largest:
        largest = int(number)


print "largest was: ", largest
