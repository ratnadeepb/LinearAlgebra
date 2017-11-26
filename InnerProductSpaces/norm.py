#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:08:50 2017

@author: ratnadeepb
@License: MIT

This modules helps find the norm of an arbitrary vector in a space of arbitrary
dimensions
"""

import numpy as np
import sys

def norm(v):
    try:
        v = np.array(v)
    except:
        sys.exit("A list, tuple or numpy array is expected")
    
    if v.ndim != 1:
        sys.exit("Not a vector")
    
    s = 0
    for e in v:
        s += np.square(e)
    
    return np.sqrt(s)

def scaled_norm(c, v):
    return abs(c) * norm(v)

def unit_vec(v):
    return v / norm(v)

if __name__ == "__main__":
    v = [3, 5]
    print("The norm of v: ", norm(v))
    print()
    print("Norm of v scaled by 2: ", scaled_norm(2, v))
    print()
    print("The unit vector in the direction of v: ", unit_vec(v))