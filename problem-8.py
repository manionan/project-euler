f = open('problem-8.txt','rU')
text = f.read()

text = text.replace('\n','')

print text

largest_start = 0
largest_product = 0
largest_string = ""
#print "len text: ", len(text)
for i in range (0,len(text)-12):

    string = text[i:i+13]
    #print "len string = ", len(string)
    product = 1

    for j in range (0,13):
        #print string[j:j+1]
        if int(string[j:j+1]) > 0:
            product *= int(string[j:j+1])
        else:
            product = 0
            continue
        
    if product> largest_product: 
        largest_string = string
        largest_product = product
      

print "largest product string: ", largest_string
print "largest product: ", largest_product
