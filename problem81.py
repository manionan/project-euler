import random

def min_sum(file_name,dim):

    n_case = 10000

    f = open(file_name,"rU")
    
    whole_file = f.read()
    whole_file = whole_file.replace('\n',',')
    
    numbers = whole_file.split(',')
    
    print numbers

    #do frontways
    movement_front = [1,dim]

    min_sum_front = 639237
    half_sum_front = {}
    for n in range(0,dim):
        for m in range(0,dim):
            half_sum_front[n,m] = min_sum_front

    for case in range(0,n_case):
        new_location = 0
        moves_each = [0,0]
        sum_numbers = int(numbers[new_location])
        choice = -1
        while (moves_each[0]<dim-1 or moves_each[1]<dim-1) and (moves_each[0]+moves_each[1])<dim-1: #last part inforces halving
            choice = -1
            if(moves_each[0]<dim-1 and moves_each[1]<dim-1):
                choice = random.randrange(0,2)
            elif(moves_each[0]<dim-1):
                choice = 0
            elif(moves_each[1]<dim-1):
                choice = 1
            if choice==-1:
                print "invalid choice!"
            moves_each[choice]+=1
            new_location += movement_front[choice]
            sum_numbers += int(numbers[new_location])
            if sum_numbers > 639237:
                break
            #print "sum moves: ",new_location
            #print "next number: ", int(numbers[new_location])
            #print "sum_numbers: ", sum_numbers
        #moves_each[choice] -=1
        if(half_sum_front[moves_each[0],moves_each[1]] > sum_numbers):
            half_sum_front[moves_each[0],moves_each[1]] = sum_numbers
        if sum_numbers < min_sum_front:
            min_sum_front = sum_numbers
    print "min sum front: ", min_sum_front
    
    #do backways
    movement_back = [-1,-dim]

    min_sum_back = 639237
    half_sum_back = {}
    for n in range(0,dim):
        for m in range(0,dim):
            half_sum_back[n,m] = min_sum_back

    for case in range(0,n_case):
        new_location = dim**2-1
        moves_each = [0,0]
        sum_numbers = int(numbers[new_location])
        choice = -1
        while (moves_each[0]<dim-1 or moves_each[1]<dim-1) and (moves_each[0]+moves_each[1])<dim-1: #last part inforces halving
            choice = -1
            if(moves_each[0]<dim-1 and moves_each[1]<dim-1):
                choice = random.randrange(0,2)
            elif(moves_each[0]<dim-1):
                choice = 0
            elif(moves_each[1]<dim-1):
                choice = 1
            if choice==-1:
                print "invalid choice!"
            moves_each[choice]+=1
            new_location += movement_back[choice]
            sum_numbers += int(numbers[new_location])
            if sum_numbers > 639237:
                break
            #print "sum moves: ",new_location
            #print "next number: ", int(numbers[new_location])
            #print "sum_numbers: ", sum_numbers
        
        #moves_each[choice] -=1
        if(half_sum_back[moves_each[0],moves_each[1]] > sum_numbers):
            half_sum_back[moves_each[0],moves_each[1]] = sum_numbers
        if sum_numbers < min_sum_back:
            min_sum_back = sum_numbers

    print "min sum back: ", min_sum_back

    min_sum = 639237
    for k,v in half_sum_front.items():
        sum = v + half_sum_back[k[1],k[0]]
        if sum<min_sum:
            min_sum = sum
        

    print "found min: ", min_sum
    
min_sum("problem81test.txt",5)
#min_sum("problem81.txt",80)
        
