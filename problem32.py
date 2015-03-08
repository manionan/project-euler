def digit_repeat_or_contain_zero(number):

    digit_used = []
    for i in range(0,10):
        digit_used.append(False)
    
    while number>0:
        digit = number % 10
        if digit == 0: return True
        if digit_used[digit] == True:
            return True
        else:
            digit_used[digit] = True
        number = int(number/10)
    
    return False

def count_digits(number):
    count = 0
    while number > 0:
        number = int(number/10)
        count += 1
    return count

#test digit tester
#print digit_repeat_or_contain_zero(12345)
#print digit_repeat_or_contain_zero(12045)
#print digit_repeat_or_contain_zero(12245)

#test count digits(number)
#print count_digits(12345)
#print count_digits(12340)

#product loop
def main():
    n_satisfy = 0
    sum = 0
    for p in range(9876,0,-1):
        if p%100 == 0: print "p = ", p
        if digit_repeat_or_contain_zero(p): continue
        number_string_p = str(p)
        for s in range(p-1,0,-1):
            if p%s != 0: continue
            f = p/s
            #if f > s: continue
            number_string = number_string_p + str(s) + str(f)
            if digit_repeat_or_contain_zero(int(number_string)): continue
            if count_digits(int(number_string)) != 9: continue
            n_satisfy +=1
            sum += p
            break #if already found product once, don't look for more

    print "n_found = ", n_satisfy
    print "sum = ", sum

#main()
