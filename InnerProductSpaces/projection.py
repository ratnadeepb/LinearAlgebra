#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:16:26 2017

@author: ratnadeepb
@License: MIT
"""

'''
This module defines a single function proj(u, v). This function returns the
orthoginal projection of the vector u on the vector v.

Similar, projections in other vector spaces can be obtained by using 
corresponding inner product definitions.

Please look at the InnerProductSPaces.Examples folder for more on such functions
'''

# System Imports
import numpy as np
import sys

# Local Imports
from InnerProductSpaces.dot import dot
from InnerProductSpaces.norm import norm

def proj(u, v):
    try:
        u = np.array(u)
        v = np.array(v)
    except:
        sys.exit("A list, tuple or numpy array is expected")
    
    return dot(u, v) * v / np.square(norm(v))

if __name__ == "__main__":
    u = [1, 2]
    v = [3, 4]
    print("The projection of u on v is: ", proj(u, v))