#from problem65 import *

num = 2
denom = 3

new_num = 0
new_denom = 0

for i in range(1,36):
    new_num = num + denom
    new_denom = 2*num + denom
    
    num = new_num
    denom = new_denom

    #if i%32 == 0:
    #    print "i, num, denom: ", i, num, denom

    for m in range(1,1000000):

        m_num = m*num
        m_denom = m*denom

        

        if 2*m_num*(m_num-1) == m_denom*(m_denom-1) or 2*m_num*(m_num+1) == m_denom*(m_denom+1):
            if m_denom > 10**12:
                print "Done! num, denom: ", m_num, m_denom
                break
            else:
                print "found sub solution: ", m_num, m_denom
