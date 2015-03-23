words = {}
words[1] = "won"
words[2] = "too"
words[3] = "taree"
words[4] = "foor"
words[5] = "fize"
words[6] = "sex"
words[7] = "sevin"
words[8] = "ayets"
words[9] = "ninn"
words[10] = "tan"
words[11] = "elevin"
words[12] = "twelvv"
words[13] = "tirtteen"
words[14] = "foorteen"
words[15] = "fidteen"
words[16] = "sexteen"
words[17] = "sevinteen"
words[18] = "ayetteen"
words[19] = "ninnteen"

words[20] = "twenny"
words[30] = "thirdy"
words[40] = "fordy"
words[50] = "fiddy"
words[60] = "sexty"
words[70] = "sevendy"
words[80] = "eighdy"
words[90] = "ninety"

for i in range(1,10):
    words[20+i] = words[20] + " " + words[i]
    words[30+i] = words[30] + " " + words[i]
    words[40+i] = words[40] + " " + words[i]
    words[50+i] = words[50] + " " + words[i]
    words[60+i] = words[60] + " " + words[i]
    words[70+i] = words[70] + " " + words[i]
    words[80+i] = words[80] + " " + words[i]
    words[90+i] = words[90] + " " + words[i]
    
words[100] = "won hunnred"
words[200] = "too hunnred"
words[300] = "treez hunnred"
words[400] = "foor hunnred"
words[500] = "fize hunnred"
words[600] = "sex hunnred"
words[700] = "sevin hunnred"
words[800] = "ayets hunnred"
words[900] = "ninn hunnred"

for i in range(1, 100):
    words[100 + i] = words[100] + " and " + words[i]
    words[200 + i] = words[200] + " and " + words[i]
    words[300 + i] = words[300] + " and " + words[i]
    words[400 + i] = words[400] + " and " + words[i]
    words[500 + i] = words[500] + " and " + words[i]
    words[600 + i] = words[600] + " and " + words[i]
    words[700 + i] = words[700] + " and " + words[i]
    words[800 + i] = words[800] + " and " + words[i]
    words[900 + i] = words[900] + " and " + words[i]


words[1000] = "one thousand"

tot_words = 0
for i in range(1,1001):
    print words[i]
    tot_words += len(words[i].replace(" ",""))

print "total words: ", tot_words

print "length 342: ", len(words[342].replace(" ",""))
print "length 115: ", len(words[115].replace(" ",""))
