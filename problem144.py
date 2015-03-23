import math

tolerance = 0.0001

#################

def find_sol(m,b,old_x,old_y):
    y = [0,0]
    x = [0,0]
    
    root_y = 100*(m**2) - (b**2)*(m**2) + 25*(m**4)
    root_y = math.sqrt(root_y)
    
    front_y = 2*b
    denom_y = 4 + m**2

    y[0] = 2*(front_y + root_y)/denom_y
    y[1] = 2*(front_y - root_y)/denom_y

    root_x = 100 - b**2 + 25*(m**2)
    root_x = math.sqrt(root_x)
    root_x *= 2

    front_x = -m*b
    denom_x = 4 + m**2

    x[0] = (front_x + root_x)/denom_x
    x[1] = (front_x - root_x)/denom_x

    sol = [0,0]
    if verify_sol(x[0], y[0], old_x, old_y):
        sol[0] = x[0]
        sol[1] = y[0]
    elif verify_sol(x[1], y[1], old_x, old_y):
        sol[0] = x[1]
        sol[1] = y[1]
    elif verify_sol(x[0], y[1], old_x, old_y):
        sol[0] = x[0]
        sol[1] = y[1]
    elif verify_sol(x[1], y[0], old_x, old_y):
        sol[0] = x[1]
        sol[1] = y[0]
    else:
        print "both invalid:", x[0], ", ", y[0], "and", x[1], ", ",  y[1]
        print "in equations are: ", 4*x[0]**2 + y[0]**2, 4*x[1]**2 + y[1]**2
        print "mixed in equations are: ", 4*x[0]**2 + y[1]**2, 4*x[1]**2 + y[0]**2
        return None
    print sol
    return sol




    
#################

def verify_sol(x, y, old_x, old_y):

    if abs(4*(x**2) + y**2 - 100) >  tolerance:
        #print "was not on ellipse"
        return False
    if abs(x - old_x) < tolerance and abs(y - old_y) < tolerance:
        #print "was same as old xy"
        return False
    return True

#test:
#print find_sol( (10.1 + 9.6)/(0.0 - 1.4), 10.1, 0, 10)
#################

def sol_to_mb(x, y, old_x, old_y):
    mb = [0,0]
    mb[0] = (y-old_y)/(x-old_x)
    mb[1] = -mb[0]*old_x + old_y
    return mb

#################
    
def find_mT(x0,y0):
    m_T = y0/(4*x0)
    return m_T

#################

def find_mb_out(m_in,m_T,x0,y0):
    m_out = (-m_in + 2*m_T + m_in*(m_T**2))
    m_out /= (1 + 2*m_in*m_T - m_T**2)

    b_out = -m_out*x0 + y0

    out = [m_out,b_out]
    return out

#################

def did_exit(x,y):
    if (y - 10) > -tolerance and abs(x) < 0.01:
        return True
    else:
        return False

#################    

def main():
    
    input_m = (10.1 + 9.6)/(0.0 - 1.4)
    input_b = 10.1

    xy = [0,10.1]
    old_xy = xy
    mb = [input_m,input_b]

    count = 0
    while count == 0 or did_exit(xy[0], xy[1]) == False:
        if count%100 == 0: print "count =", count

        xy = find_sol(mb[0],mb[1],old_xy[0],old_xy[1])
        
        mT = find_mT(xy[0],xy[1])

        mb = find_mb_out(mb[0],mT,xy[0],xy[1])

        old_xy = xy

        count += 1

    print "final count: ", count

main()
