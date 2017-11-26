#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:48:39 2017

@author: ratnadeepb
@License: MIT
"""

# System Import
import numpy as np
import sys

# Local Import
from InnerProductSpaces.norm import unit_vec
from InnerProductSpaces.projection import proj

'''
Gram Schmidt process of creating orthonormal basis from an arbitrary basis
'''

def gram_schmidt(B):
    try:
        B = np.array(B, dtype=np.float16)
    except:
        sys.exit("Not a vector")
    
    W = np.zeros_like(B)
    
    # Create and orthogonal basis
    W[0] = B[0]
    i = 1
    while i < len(B):
        p = 0
        j = 1
        while j < i:
            p += proj(B[j], W[i - 1])
            j += 1
        W[i] = B[i] - p
        i += 1
    
    # Normalise
    U = np.zeros_like(W)
    for ind, w in enumerate(W):
        temp = unit_vec(w)
        for s, u in enumerate(temp):
            U[ind][s] = u
    
    return U

if __name__ == "__main__":
    B = [[0, 1, 1],
         [2, 1, 0],
         [-1, 0, -1]]
    U = gram_schmidt(B)
    print(U)
    '''
    U = [[0, 1/np.sqrt(2), 1/np.sqrt(2)],
          [2/np.sqrt(6), 1/np.sqrt(6), -1/np.sqrt(6)],
          [-1/np.sqrt(3), 1/np.sqrt(3), -1/np.sqrt(3)]]
    '''