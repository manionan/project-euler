def count_chars(file):
    f = open(file,"rU")
    chars = 0
    n_lines = 0
    for line in f:
        chars += len(line.strip("\n"))
        n_lines += 1

    return chars

singles = {}

#singles
singles["I"] = 1
singles["V"] = 5
singles["X"] = 10
singles["L"] = 50
singles["C"] = 100
singles["D"] = 500
singles["M"] = 1000

doubles = {} 

#doubles
doubles["IV"] = 4
doubles["IX"] = 9
doubles["XL"] = 40
doubles["XC"] = 90
doubles["CD"] = 400
doubles["CM"] = 900

def convert_numeral2int(numeral):
    integer = 0
    cut_numeral = numeral
    prev_numeral = cut_numeral

    while True: #cut until no more cuts
        prev_numeral = cut_numeral

        for key in doubles.keys():
            if cut_numeral != cut_numeral.replace(key,'',1):
                cut_numeral = cut_numeral.replace(key,'',1)
                integer += doubles[key]

        if prev_numeral == cut_numeral:
            break

    while True:
        prev_numeral = cut_numeral

        for key in singles.keys():
            if cut_numeral != cut_numeral.replace(key,'',1):
                cut_numeral = cut_numeral.replace(key,'',1)
                integer += singles[key]
        
        if prev_numeral == cut_numeral:
            break

    return integer

#test
print convert_numeral2int("MMMMDCLXXII")
print convert_numeral2int("MDCCCXVIII")

#read in number to numeral list
f2 = open("roman_numerals_list.csv","rU")

number2numeral = {}

for line in f2:
    no_newline = line.strip('\n')
    key_val = no_newline.split(',')
    number2numeral[int(key_val[0])] = key_val[1]

#do main thing
fout = open("p089_solution.txt","w")
fin  = open("p089_roman.txt","rU")

for line in fin:
    numeral = line.strip('\n')
    number = convert_numeral2int(numeral)
    new_numeral = number2numeral[number]
    fout.write(new_numeral)
    fout.write("\n")

fout.close()
fin.close()


before =  count_chars("p089_roman.txt")
after = count_chars("p089_solution.txt")

print "before, after, diff: ", before, after, before-after
