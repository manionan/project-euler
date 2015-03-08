
replacements = {}

######################
###SUBTRACTIVE REPLACEMENTS
######################

##I, V replacements
replacements["IIII"] = "IV"

##I, X replacements
replacements["IIIIIIIII"] = "IX"
replacements["IIIIIIII"]  = "IIX"
replacements["IIIIIII"]   = "IIIX"
replacements["IIIIII"]    = "IIIIX"

##X,L replacements
replacements["XXXX"] = "XL"

##X,C replacements
replacements["XXXXXXXXX"] = "XC"
replacements["XXXXXXXX"]  = "XXC"
replacements["XXXXXXX"]   = "XXXC"
replacements["XXXXXX"]    = "XXXXC"

##C,D replacements
replacements["CCCC"] = "CD"

##C,M replacements
replacements["CCCCCCCCC"] = "CM"
replacements["CCCCCCCC"]  = "CCM"
replacements["CCCCCCC"]   = "CCCM"
replacements["CCCCCC"]    = "CCCCM"

######################
###ADDITIVE REPLACEMENTS
######################
replacements["IIIII"] = "V"
replacements["XXXXX"] = "L"
replacements["CCCCC"] = "D"

######################
###ILLEGALS REPLACEMENTS
######################
replacements["VV"] = "X"
replacements["LL"] = "C"
replacements["DD"] = "M"


def main():
    f = open("p089_roman.txt","rU")

    chars = 0
    n_lines = 0
    for line in f:
        chars += len(line.strip("\n"))
        if n_lines == 0:
            print line
            print chars
        n_lines += 1

    print "original chars: ", chars

    for line in f:
        prev_numeral = line.strip("\n")
        length = len(prev_numeral)
        while length > 1:
            
    
