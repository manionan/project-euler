def list_digits(n):
    listy = []
    n_digits = 0

    m = n
    while m > 0:
        m /= 10
        n_digits += 1

        

    for i in range(0,n_digits):
        listy.append( (n / 10**i) % 10 )
    
    listy.reverse()

    return listy

print list_digits(12345)
print list_digits(90089)
print list_digits(1)

count = 0
n = 1
ch = []
while count < 10**6:
    for d in list_digits(n):
        ch.append(d)
        count += 1
    n += 1


product = ch[0]*ch[9]*ch[99]*ch[999]*ch[9999]*ch[99999]*ch[999999]
print product
