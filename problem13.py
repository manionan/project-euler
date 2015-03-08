f = open("problem13.txt","rU")

column_sum = []
for i in range(0,50):
    column_sum.append(0)

for line in f:
    for i in range(0,50):
        column_sum[49-i] += int( line[i:i+1] )

for i in range(0,49):
    column_sum[i+1] += column_sum[i]/10
    column_sum[i] = column_sum[i]%10
end_sum = column_sum[49]/10
column_sum[49] = column_sum[49]%10
    
print "end sum is: ", end_sum
print "next 8 digits are: ", column_sum[49], column_sum[48], column_sum[47], column_sum[46], column_sum[45], column_sum[44], column_sum[43], column_sum[42]
