limit = 10000
over_limit = 25321

max_over = 0
def sum_divisors(number):
    global max_over
    sum = 0
    
    for i in range(1,number):
        if number % i == 0:
            sum += i

    return sum


func_d = {}
for i in range(1,over_limit):
    func_d[i] = sum_divisors(i)

print "done"

am = []
n_am = 0
sum_am = 0
for i in range(2,limit):
    if func_d[i] < 0: 
        print "didn't have divisor"
        continue
    if func_d[i] == 0:
        print "zero at", i
        continue
    if func_d[i] == i:
        print "dooble number"
        continue
    if func_d[func_d[i]] == i:
        am.append(i)
        n_am +=1
        sum_am += i

print "total amicable = ", n_am
print "sum amicable = ", sum_am
print "list: ", am

new_sum = 0
for a in am:
    new_sum += a

print "new sum: ", new_sum
