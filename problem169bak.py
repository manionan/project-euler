num = 10**25
num = 16
num = 10
i = 83
pow_list = []
while num > 0:
    if i < 0:
        break
    if 2**i <= num:
        num -= 2**i
        pow_list.append(i)
        i -= 1
        print num
    else:
        i -= 1

print pow_list

print "length power list:", len(pow_list)

can_dec = []
for i in range(len(pow_list) - 1):
    if (pow_list[i] - pow_list[i+1]) > 1:
        can_dec.append(True)
    else:
        can_dec.append(False)

print can_dec
sum_ways = 0

def count_ways_rec(indx, curr_ways, dec = False):
    global sum_ways
    
    pow_mod = 0
    if dec:
        pow_mod = 1

    #end case
    if indx > (len(pow_list) - 1):#went too far
        return
    if indx == (len(pow_list) - 1):# if on last element
        if pow_list[indx] - pow_mod < 0:#went too far
            return
        elif pow_list[indx] - pow_mod == 0:#last element cannot be moved
            sum_ways += curr_ways
            print "was exactly zero and added", curr_ways
        else:
            new_ways = curr_ways * (pow_list[indx] - pow_mod + 1)#last element can be moved, even to 0
            sum_ways += new_ways
            print "was gt zero and added", new_ways, "with curr_ways:", curr_ways
        return

    #continue to smaller powers...
    #...with next original
    if (pow_list[indx] - pow_mod - pow_list[indx + 1]) > 0: #otherwise not allowed
        new_ways = curr_ways * (pow_list[indx] - pow_mod - pow_list[indx + 1])
        count_ways_rec(indx+2, new_ways)
        
    #...with next moved down
    if (pow_list[indx] - pow_mod - pow_list[indx + 1] + 1) > 0: #otherwise not allowed
        new_ways = curr_ways * (pow_list[indx] - pow_mod - pow_list[indx + 1] + 1)
        count_ways_rec(indx+1, new_ways, True)
        

        

count_ways_rec(0,1)

print sum_ways
