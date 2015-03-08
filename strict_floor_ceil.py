import math
def strict_floor(f):
    
    if math.floor(f) == f:
        return int(f - 1)
    else: 
        return math.floor(f)
    
def strict_ceil(f):
    if math.ceil(f) == f:
        return int(f + 1)
    else:
        return math.ceil(f)
