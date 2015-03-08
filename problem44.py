import math
def is_power(n):
    int_root = int(math.sqrt(n))
    if int_root*int_root == n:
        return True
    else:
        return False

def find_smallest_D(max_m,max_n):
    
    two_D_min = 3*(max_n**2) - max_n
    
    for n in range(1,max_n):
        for m in range(n+1,max_m):

            c1 = 3*(m**2 + n**2) - (m + n)
            sq1 = 1 + 6*c1
            if is_power(sq1) == False:
                continue
            p_num = 1 + math.sqrt(sq1)
            if p_num % 6 != 0:
                continue

            c2 = 3*(m**2 - n**2) - (m - n)
            sq2 = 1 + 6*c2
            if is_power(sq2) == False:
                continue
            q_num = 1 + math.sqrt(sq2)
            if q_num % 6 != 0:
                continue

            two_D = 3*(n**2) - n
            if two_D % 2 != 0:
                continue
            
            if two_D < two_D_min:
                two_D_min = two_D
                print "min candidate: ", two_D/2
            
    print "found min D: ", two_D_min/2

find_smallest_D(10000,10000)
