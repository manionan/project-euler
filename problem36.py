from problem4 import *

binary_test = bin(585)
binary_test = binary_test.lstrip("0b")
print int(binary_test)

def find_sum_palindrome():
    sum_palindrome = 0
    for i in range (1,10**6):
        
        if i%10 == 0: #palindrome can't end in 0
            continue
            
        #check regular
        digits = digit_count(i)
        n_to_check = digits/2
        first = get_first(i,n_to_check)
        last = get_last_reversed(i,n_to_check)

        if first != last:
            continue

        #now check binary
        binary_i = bin(i)
        binary_i = binary_i.lstrip("0b")
        binary_i = int(binary_i)
        
        if binary_i%10 == 0: #palindrome can't end in 0
            continue

        binary_digits = digit_count(binary_i)
        binary_n_to_check = binary_digits/2
        binary_first = get_first(binary_i,binary_n_to_check)
        binary_last = get_last_reversed(binary_i,binary_n_to_check)

        if binary_first != binary_last:
            continue
            
        sum_palindrome += i
        
        #print i, binary_i

    return sum_palindrome

print find_sum_palindrome()
