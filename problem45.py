import math
def is_power(n):
    int_root = int(math.sqrt(n))
    if int_root*int_root == n:
        return True
    else:
        return False

def find_common(max_r):

    for r in range(144,max_r):

        c = 2*r*(2*r - 1)

        sq1 = 1 + 4*3*c
        if is_power(sq1) == False:
            continue
        q_num = 1 + math.sqrt(sq1)
        if q_num % 6 != 0:
            continue

        sq2 = 1 + 4*c
        if is_power(sq2) == False:
            continue
        p_num = -1 + math.sqrt(sq2)
        if p_num % 2 != 0:
            continue

        hex_num = r*(2*r - 1)
        return hex_num

print find_common(1000000)
