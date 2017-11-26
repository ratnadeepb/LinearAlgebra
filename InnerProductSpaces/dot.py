#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:39:40 2017

@author: ratnadeepb
@License: MIT
"""

# System Imports
import numpy as np
import sys

def dot(u, v):
    try:
        u = np.array(u)
        v = np.array(v)
    except:
        sys.exit("A list, tuple or numpy array is expected")
    
    if u.ndim != 1 and v.ndim != 1:
        sys.exit("Not a vector")
    
    s = 0
    for i, j in zip(u, v):
        s += i * j
    
    return np.sum(s)

if __name__ == "__main__":
    u = [1, 2]
    v = [3, 4]
    print("The dot product of u and v is: ", dot(u, v))