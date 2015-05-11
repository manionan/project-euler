#!/usr/bin/python

import sys, math

def main(number):
    pow_list = []
    num = int(number)
    i = 0
    test_pow = 1
    while test_pow < num:
        i += 1
        test_pow = 2**i
    
    while num > 0:
        if i < 0:
            break
        if 2**i <= num:
            num -= 2**i
            pow_list.append(i)
            i -= 1
        else:
            i -= 1

    print pow_list

if __name__ == "__main__":
    main(sys.argv[1])
