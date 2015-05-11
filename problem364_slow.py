sum_counts = 0
def rec_count_seats(seat_vals,n_seats):
    global sum_counts
    #first look for seats with no neighbors and take them
    has_three = False
    for i in range(0,n_seats):
        if seat_vals[i] == 3:
            has_three = True
            new_vals = list(seat_vals)
            new_vals[i] = 0
            if i-1 >= 0:
                if new_vals[i-1] > 0: 
                    new_vals[i-1] -= 1
            if i+1 < n_seats:
                if new_vals[i+1] > 0:
                    new_vals[i+1] -= 1
            #print new_vals
            rec_count_seats(new_vals,n_seats)

        #if no neighborless seats left, look for one neighbor seats

    if not has_three:
        has_two = False
        for i in range(0,n_seats):
            if seat_vals[i] == 2:
                has_two = True
                new_vals = list(seat_vals)
                new_vals[i] = 0
                if i-1 >= 0:
                    if new_vals[i-1] > 0: 
                        new_vals[i-1] -= 1
                if i+1 < n_seats:
                    if new_vals[i+1] > 0:
                        new_vals[i+1] -= 1
                #print new_vals
                rec_count_seats(new_vals,n_seats)

        #if no one-neighbor seats, fill remaining seats
        if not has_two:
            has_one = False
            for i in range(0,n_seats):
                if seat_vals[i] == 1:
                    has_one = True
                    new_vals = list(seat_vals)
                    new_vals[i] = 0
                    if i-1 >= 0:
                        if new_vals[i-1] > 0: 
                            new_vals[i-1] -= 1
                    if i+1 < n_seats:
                        if new_vals[i+1] > 0:
                            new_vals[i+1] -= 1
                    #print new_vals
                    rec_count_seats(new_vals,n_seats)

            #if no more seats left, update counts
            if not has_one:
                sum_counts += 1
                return
                #print seat_vals
                #print "######################"

def problem_364(n_seats,occupied_end = False):
    global sum_counts
    seat_vals = []
    for i in range(0,n_seats):
        seat_vals.append(3)
    if occupied_end:
        seat_vals[0] = 2

    sum_counts = 0
    rec_count_seats(seat_vals,n_seats)
    return sum_counts

answer_list = []
sum_list = []
running_sum = 0
for i in range(1,14):
    result = problem_364(i)
    #print "########"
    #print "running sum: ", running_sum
    print "n =", i, "gives", result
    #print "result/(running_sum + 1.0):", result, "/", running_sum + 1.0
    
    floor = result / (running_sum + 1)

    #print "floor is: ", floor
    difference = result - (running_sum + 1)*floor
    sum_list.append((running_sum+1)*floor)
    running_sum += result

    answer_list.append(result)


print answer_list
print sum_list
