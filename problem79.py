f = open('p079_keylog.txt','rU')

#test list function


nums_left_of = {}
nums_right_of = {}

for digit in range(0,10):
    if digit == 4 or digit == 5:
        continue
    nums_left_of[digit] = []
    nums_right_of[digit] = []

for line in f:
    str = line.strip('\n')
    i = list(str)
    
    #left number
    if nums_right_of[int(i[0])].count(int(i[1])) == 0:
        nums_right_of[int(i[0])].append(int(i[1]))
    
    if nums_right_of[int(i[0])].count(int(i[2])) == 0:
        nums_right_of[int(i[0])].append(int(i[2]))

    #center number
    if nums_left_of[int(i[1])].count(int(i[0])) == 0:
        nums_left_of[int(i[1])].append(int(i[0]))
    
    if nums_right_of[int(i[1])].count(int(i[2])) == 0:
        nums_right_of[int(i[1])].append(int(i[2]))

    #right number
    if nums_left_of[int(i[2])].count(int(i[0])) == 0:
        nums_left_of[int(i[2])].append(int(i[0]))
    
    if nums_left_of[int(i[2])].count(int(i[1])) == 0:
        nums_left_of[int(i[2])].append(int(i[1]))

rank_R = [-1,-1,-1,-1,-1,-1,-1,-1]

for key in nums_right_of.keys():
    if len(nums_right_of[key]) == None:
        rank_R[0] = key
    else:
        rank_R[len(nums_right_of[key])] = key

rank_R.reverse()

rank_L = [-1,-1,-1,-1,-1,-1,-1,-1]

for key in nums_left_of.keys():
    if len(nums_left_of[key]) == None:
        rank_L[0] = key
    else:
        rank_L[len(nums_left_of[key])] = key

print rank_R
print rank_L

