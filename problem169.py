num = 10**25
#num = 32
#num = 10
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

def count_ways_rec(indx, curr_ways, dec = 0):
    global sum_ways
    
    #end cases:
    if indx > len(pow_list) - 1: #can't go here
        sum_ways += curr_ways
        return
    elif pow_list[indx] - dec < 0: #cant decrement below zero
        return
    elif indx == len(pow_list) - 1:
        new_ways = curr_ways * (pow_list[indx] + 1 - dec)#add one since 0 allowed 
        #print "####"
        #print "with dec?", dec
        #print "old + new:", sum_ways, new_ways
        #print "broken up:", curr_ways, new_ways/curr_ways
        sum_ways += new_ways

        return

    #don't move the next one down
    if pow_list[indx] - dec > pow_list[indx+1]: 
        new_ways = curr_ways*(pow_list[indx] - dec - pow_list[indx+1])
        #print "new ways in outer loop:", new_ways
        count_ways_rec(indx + 2, new_ways, 0) #without next-next one decremented
    #move the next one down 
    if pow_list[indx] - dec > pow_list[indx+1] - 1:
        new_ways = curr_ways*(pow_list[indx] - dec - pow_list[indx+1] + 1)
        count_ways_rec(indx + 1, new_ways, 1) #with next one decremented
        
        

        

count_ways_rec(0,1)

print sum_ways
