#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:35:07 2017

@author: ratnadeepb
@License: MIT
"""

'''
Let c[0, 1] be the space of all continuous real valued functions in the interval
[0, 1].

Let f(x) = x + 1
and g(x) = 2 + x^2

Inner Product is defined as the definite integral of f(x) * g(x) in the interval
0 to 1.
'''

import sympy
import numpy as np
import sys

# Function dot product
def fn_dot(f, g, upper, lower):
    try:
        return sympy.N(sympy.integrate(f*g, (x, lower, upper)))
    except:
        sys.exit("Problem not formatted correctly")
        
# Function norm
def fn_norm(f, upper, lower):
    return np.sqrt(float(fn_dot(f, f, upper, lower)))

# Angle between two functions
def fn_angle(f, g, upper, lower, op="radians"):
    if op not in ["radians", "degrees"]:
        sys.exit("At this time we only handle radians and degrees")
    return np.arccos(float(fn_dot(f, g, upper, lower) / (fn_norm(f, upper, 
                           lower) * fn_norm(g, upper, lower))))

if __name__ == "__main__":
    upper = 1
    lower = 0
    
    x = sympy.symbols('x')
    
    f = x + 1
    g = x**2 + 2
    
    print("The inner product of the functions is: ", fn_dot(f, g, upper, lower))
    print("The norm of f is: ", fn_norm(f, upper, lower))
    print("The angle between the functions is: ", fn_angle(f, g, upper, lower))