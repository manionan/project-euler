import math

def find_path_max(file):

    f = open(file,"rU")
    


    # make list of dicts, read in file, also count lines in file
    pyramid_list = {}
    n_lines = 0
    for line in f:

        #pyramid_list.append(empty_dict)
        line_list = line.split(',')

        #fill dict
        item_inc = 0
        for i in range(n_lines,-n_lines - 1, -2):
            pyramid_list[n_lines,i] = int(line_list[item_inc])
            item_inc += 1

        n_lines +=1

    #print pyramid_list


    #now find maximum path sum through pyramid
    for i in range(1,n_lines):
        for j in range(i, -i -1, -2):
            if j == i:
                pyramid_list[i,j] += pyramid_list[i-1,j-1]
            elif j == -i:
                pyramid_list[i,j] += pyramid_list[i-1,j+1]
            else:
                pyramid_list[i,j] += max( pyramid_list[i-1,j-1], 
                                           pyramid_list[i-1,j+1])
        
    #find max in last row
    maxi = 0
    for j in range(n_lines -1, -n_lines, -2):
        if pyramid_list[n_lines-1,j] > maxi:
            maxi = pyramid_list[n_lines-1,j]

    print "found max of :", maxi
    
    #print pyramid_list

find_path_max("problem18simp.txt")
find_path_max("problem18.txt")
find_path_max("p067_triangle.txt")
