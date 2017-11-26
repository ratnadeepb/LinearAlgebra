#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:53:40 2017

@author: ratnadeepb
@License: MIT
"""

# System Imports
import numpy as np
import sys

# Local imports
from InnerProductSpaces.dot import dot
from InnerProductSpaces.norm import norm

def angle(u, v, op="radians"):
    n_u = norm(u)
    n_v = norm(v)
    
    if op not in ("radians", "degrees"):
        sys.exit("At this time we only handle radians and degrees")
    
    # The angle does not exist if one of them is a zero vector
    if n_u == 0 or n_v == 0:
        return np.NaN
    
    a = np.arccos(dot(u, v) / (norm(u) * norm(v)))
    
    if op == "radians":
        return a
    else:
        return a * (180 / np.pi)

if __name__ == "__main__":
    # u = [6, 2]
    u = (-3, 3)
    # v = [1, 4]
    v = (5, 5)
    a_r = angle(u, v)
    if np.isnan(a_r):
        print("The angle does not exist")
    else:
        a_d = angle(u, v, "degrees")
        print("The angle between u and v is {} radians".format(np.round(a_r, 
              decimals=4)))
        print("This is the same as {} degrees".format(np.round(a_d, 
              decimals=4)))