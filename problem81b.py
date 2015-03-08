def min_sum(file_name,dim):
    f = open(file_name,"rU")
    
    whole_file = f.read()
    whole_file = whole_file.replace('\n',',')
    
    string_numbers = whole_file.split(',')
    numbers = []
    for string in string_numbers:
        if string!='':
            numbers.append(int(string))
    mins = []
    for i in range(0,len(numbers)):
        mins.append(0)

    mins[0] = numbers[0]

    #make list of movement choices
    movement = [1,dim]

    #propagate minimum
    for i in range(1,dim**2):
        if i < dim: #top row
            mins[i] = numbers[i] + mins[i-movement[0]]
        elif i%dim == 0: # left column
            mins[i] = numbers[i] + mins[i-movement[1]]
        else: #other cases
            mins[i] = numbers[i] + min(mins[i-movement[0]], mins[i-movement[1]])
       

    print "final min is:", mins[dim**2 - 1]
min_sum("problem81test.txt",5)
min_sum("problem81.txt",80)
        
