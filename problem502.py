def count_castles_w4(h):
    n_castles = 0
    for a in range(1,h+1):
        height_achieved_a = False
        if a == h: height_achieved_a = True

        for b in range(1,h+1):
            height_achieved_b = False
            if b == h: height_achieved_b = True

            for c in range(1,h+1):
                height_achieved_c = False
                if c == h: height_achieved_c = True

                for d in range(1,h+1):
                    height_achieved_d = False
                    if d == h: height_achieved_d = True
                    if height_achieved_a or height_achieved_b or height_achieved_c or height_achieved_d:
                        n_castles +=1
    print "n_castles: ", n_castles

count_castles_w4(2)
            
