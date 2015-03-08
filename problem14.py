has_chain = {}
chain_length = {}

for i in range(2,18076285):
    has_chain[i] = False
    chain_length[i] = 0

max_length = 0
max_number = 0

for i in range(2,1000000):

    count = 1
    j = i

    while j>1:

        if(j<18076285):
            if has_chain[j]:
                count += chain_length[j] - 1
                break

        if j%2==0:
            j = j/2
        else:
            j = 3*j+1

        count +=1
    
    has_chain[i] = True
    chain_length[i] = count

    if count > max_length:
        max_length = count
        max_number = i

print "max length: ", max_length
print "max number: ", max_number
