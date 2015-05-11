import math

n_rounds = 15
n_min = int(math.floor(n_rounds/2.0)) + 1


probs = []

term = 1.0
for i in range(0,n_rounds):
    term = 1.0/(2.0 + i)
    #term *= (2 + i)
    probs.append(term)

print probs

list_enum = []
index_list = []
for i in range(0,n_rounds):
    index_list.append(i)

index_list.sort()

def rec_loop(my_list, lim, depth, n_loop, items):


    if n_loop > 0 and depth < lim:
        #delve deeper
        for i in range(depth,lim):
            new_items = list(items)
            new_items.append(my_list[i]) 
            rec_loop(my_list, lim, i + 1, n_loop - 1, new_items)

    elif n_loop == 0:
        list_enum.append(items)

        

for n in range(n_min,n_rounds + 1):
    choice_items = []
    rec_loop(index_list, n_rounds, 0, n, choice_items)
#print list_enum
   
summy = 0
for sublist in list_enum:
    product = 1.0
    #print "*****"
    #print sublist
    for i in range(0,n_rounds):
        if i in sublist:
            #print i
            product *= probs[i]
        else:
            product *=  (1.0 - probs[i])
    summy += product 

print summy

print "answer: ", int((1-summy)/summy) + 1

print 11.0/120.0

print "###choose1:"
print (2**4 * 3**3 * 4**2 * 5)

print "###choose3: "
print (2**3 * 3**2 * 4)
print (2**3 * 3**2 * 4 * 5)
print (2**3 * 3**2 * 4**2 * 5)
print (2**3 * 3**3 * 4**2 * 5)

print "##choose2:"
print (2**2 * 3)
print (2**2 * 3 * 4)
print (2**2 * 3 * 4 * 5)
print (2**2 * 3**2 * 4)
print (2**2 * 3**2 * 4 * 5)
print (2**2 * 3**2 * 4**2 * 5)
