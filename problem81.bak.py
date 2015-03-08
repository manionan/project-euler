import random

def min_sum(file_name,dim):
    f = open(file_name,"rU")
    
    whole_file = f.read()
    whole_file = whole_file.replace('\n',',')
    
    numbers = whole_file.split(',')
    
    #make list of movement choices
    movement = [1,dim]

    min_sum = 639237

    for case in range(0,1000000):
        new_location = 0
        moves_each = [0,0]
        sum_numbers = int(numbers[0])
        
        while (moves_each[0]<dim-1 or moves_each[1]<dim-1):# and (moves_each[0]+moves_each[1])<dim-1:
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
            new_location += movement[choice]
            sum_numbers += int(numbers[new_location])
            if sum_numbers > 639237:
                break
            #print "sum moves: ",new_location
            #print "next number: ", int(numbers[new_location])
            #print "sum_numbers: ", sum_numbers
        if sum_numbers < min_sum:
            min_sum = sum_numbers
    print "found min: ", min_sum
            
#min_sum("problem81test.txt",5)
min_sum("problem81.txt",80)
        
