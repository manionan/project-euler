file = open('problem11.txt','rU')

lines = []

line_counter = 0
for file_line in file:
    numbers = []
    for i in range(0,len(file_line)-2,3):
        numbers.append( int( file_line[i:i+3] ))
    lines.append(numbers)
    line_counter += 1

print "number of lines in file: ", line_counter
print "length of line: ", len(lines[0])

product = 0
max_product = 0
for l in range(0,line_counter):
    for n in range(0,len(lines[0])):
        #do right
        if n+3 < len(lines[0]):
            product = lines[l][n]*lines[l][n+1]*lines[l][n+2]*lines[l][n+3]
            if product > max_product:
                max_product = product
        #do down
        if l+3 < line_counter:
            product = lines[l][n]*lines[l+1][n]*lines[l+2][n]*lines[l+3][n]
            if product > max_product:
                max_product = product
        #do diagonal right
        if l+3 < line_counter and n+3 < len(lines[0]):
            product = lines[l][n]*lines[l+1][n+1]*lines[l+2][n+2]*lines[l+3][n+3]
            if product > max_product:
                max_product = product
        #do diagonal left
        if l+3 < line_counter and n-3 > 0:
            product = lines[l][n]*lines[l+1][n-1]*lines[l+2][n-2]*lines[l+3][n-3]
            if product > max_product:
                max_product = product

print "max product was: ", max_product
