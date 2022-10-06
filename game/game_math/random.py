from math import floor
import random
import numpy as np

def RandomRange(x,y):
    return random.randrange(x,y)

def RandomNormalClamped(mu, sig, min_val, max_val):
    ret_val = np.random.normal(mu, sig)
    ret_val = floor(ret_val)
    ret_val = Clamp(ret_val, min_val, max_val)
    return ret_val

def Clamp(val, min_val, max_val):
    return min(max_val, max(min_val, val))