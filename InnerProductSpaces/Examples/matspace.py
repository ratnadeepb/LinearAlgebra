#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:13:40 2017

@author: ratnadeepb
@License: MIT
"""

'''
Square matrices (n x n) are also vector space where an inner product can 
be defined.

In M2,2 space let:
    A = [[a11, a21], [a12, a22]]
    B = [[b11, b21], [b12, b22]]
    
Inner Product in M2,2:
    <A, B> = a11*b11 + a21*b21 + a12*b12 + a22*b22
'''

import numpy as np
import sys

# Dot product of A and B
def mat_dot(A, B):
    try:
        A = np.array(A)
        B = np.array(B)
    except:
        sys.exit("Not compatible")
    
    bl = A.ndim == B.ndim
    if not bl:
        sys.exit("Not compatible")
    s = 0
    for i in range(A.ndim):
        for a, b in zip(A[i], B[i]):
            s += a * b
    return s

# Norm of a Matrix
def mat_norm(A):
    return np.sqrt(mat_dot(A, A))

# Angle between two matrices
def mat_angle(A, B, op="radians"):
    if op not in ["radians", "degrees"]:
        sys.exit("At this time we only handle radians and degrees")
    if op == "degrees":
        return (mat_dot(A, B) / (mat_norm(A) * mat_norm(B))) * (180 / np.pi)
    else:
        return (mat_dot(A, B) / (mat_norm(A) * mat_norm(B)))

if __name__ == "__main__":
    A = [[11, -10], [4, 3]]
    B = [[8, 7], [9, 16]]

    print("Dot product of these matrices is:", mat_dot(A, B))
    print("Angle betwee the matrices is:", mat_angle(A, B, "degrees"))