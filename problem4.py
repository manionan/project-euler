# for fun, find palindromes without using strings

def digit_count(integer):
    n_digit = 0
    divvied = integer
    while divvied >= 1:
        n_digit += 1
        divvied /= 10
    return n_digit

def get_first(integer, n_digits):
    total_digits = digit_count(integer)
    n_to_rid = total_digits - n_digits
    if n_to_rid < 0:
        print "get_first: n_digits too large for integer."
        print "n_digits: ", n_digits, "integer: ", integer
        return None
    return integer / (10**n_to_rid)

def reverse_integer(integer):
    new_number = 0
    total_dig = digit_count(integer)
    i = total_dig
    while i > 0:
        new_number += ( integer % (10**i) ) / ( 10**(i-1) ) * ( 10**(total_dig - i) )
        i -= 1
    return new_number

#print reverse_integer(123456)
#print reverse_integer(100000)

def get_last_reversed(integer, n_digits):
    integer_reversed = reverse_integer(integer)
    last_reversed = get_first(integer_reversed,n_digits)
    return last_reversed



def find_palindrome():
    largest_palindrome = 0
    for i in range (100,1000):
        for j in range (100,1000):
            product = i*j
            if product%10 == 0: #palindrome can't end in 0
                continue
            digits = digit_count(product)
            n_to_check = digits/2
            first = get_first(product,n_to_check)
            last = get_last_reversed(product,n_to_check)
            if first == last:
                if product > largest_palindrome:
                    largest_palindrome = product
                
    return largest_palindrome

#print find_palindrome()
