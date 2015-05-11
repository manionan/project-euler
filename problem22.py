###READ IN:

names_list = []

f = open("p022_names.txt","rU")

for line in f:
    line_list = line.split(',')
    for item in line_list:
        names_list.append(item[1:-1])

names_list.sort()
print names_list

##COMPUTE SCORES
value = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8,
         "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, 
         "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, 
         "W":23, "X":24, "Y":25, "Z":26}
def letters_score(name):
    score = 0
    for s in name:
        score += value[s]

    return score

total_scores = 0

indx = 1
for name in names_list:
    total_scores += indx*letters_score(name)
    indx += 1

print "total scores:", total_scores
