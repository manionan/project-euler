def digit_sum(number):
    sum = 0
    while number > 0:
        digit = number%10
        sum += digit
        number = int(number/10)
        
    return sum

#get sum of sequence unit:
print "sequence unit digit sum: ", digit_sum(123432)

s_unit = [1,2,3,4,3,2]
def main(term_limit):
    next_spot = 0
    

    
