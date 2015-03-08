def sum_sq_digits(n):
    sum = (n % 10)**2
    n /= 10
    while n > 0:
        sum += (n % 10)**2
        n /= 10
    return sum

def find_n89():
    found_end = {}
    end = {}

    for i in range(1, 10000000):
        found_end[i] = False

    found_end[1] = True
    end[1] = 1
    found_end[89] = True
    end[89] = 89


    n_89 = 0
    for i in range(1, 10000000):
        if i%1000 == 0:
            print i
        link = i

        while found_end[link] == False:
            link = sum_sq_digits(link)
            #print link

        found_end[i] = True
        end[i] = end[link]

        if end[i] == 89:
            n_89 += 1

    print "number ending in 89: ", n_89


find_n89()
