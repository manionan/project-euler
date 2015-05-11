num = 1
denom = 1
for x1 in range(1,10):
    for x2 in range(0,10):
        for y1 in range(1,10):
            for y2 in range(0,10):
                if y1*(10*x1 + x2) == x1*(10*y1 + y2):
                    if x2 !=0 and y2 != 0 and y1 > x1 and x2 == y2:
                        print "found", x1, "/", y1
                        print "=====>", (10*x1 + x2), "/", (10*y1 + y2)
                elif y2*(10*x1 + x2) == x2*(10*y1 + y2):
                    if x1 !=0 and y1 != 0 and y2 > x2 and x1 == y1:
                        print "found", x2, "/", y2
                        print "=====>", (10*x1 + x2), "/", (10*y1 + y2)
                elif y2*(10*x1 + x2) == x1*(10*y1 + y2):
                    if x2 !=0 and y1 != 0 and y2 > x1 and x2 == y1:
                        print "found", x1, "/", y2
                        print "=====>", (10*x1 + x2), "/", (10*y1 + y2)
                elif y1*(10*x1 + x2) == x2*(10*y1 + y2):
                    if x1 !=0 and y2 != 0 and y1 > x2 and x1 == y2:
                        print "found", x2, "/", y1
                        print "=====>", (10*x1 + x2), "/", (10*y1 + y2)
