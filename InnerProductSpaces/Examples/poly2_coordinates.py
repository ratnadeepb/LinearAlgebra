#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:16:36 2017

@author: ratnadeepb
@License: MIT
"""

# System Imports
import numpy as np

# Local Imports
from InnerProductSpaces.dot import dot

# Orthonormal basis in P2
# B = {1/sqrt(2) - x/sqrt(2), 
#       x**2, 
#       1/sqrt(2) + x/sqrt(2)}

B = [[1/np.sqrt(2), -1/np.sqrt(2), 0],
      [0, 0, 1],
      [1/np.sqrt(2), 1/np.sqrt(2), 0]]

# Find coordinates of f = -4 + 7x + 11x^2
f = [-4, 7, 11]

c = []
upper = 0
lower = 1

for b in B:
    c.append(dot(f, b))

print("The coefficients of f in P2 with the given basis B are:", c)