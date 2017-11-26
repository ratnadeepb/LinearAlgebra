#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 15:05:25 2017

@author: ratnadeepb
@License: MIT
"""

'''
This is an example demonstrating inner product in polynomials of degree 2 or 
less. This is a vector space known as P2.

Let
    p(x) = a0 + a1*x + a2*x^2
    q(x) = b0 + b1*x + b2*x^2

Inner Product:
    <p, q> = a0*b0 + a1*b1 + a2*b2
'''

from InnerProductSpaces.dot import dot
from InnerProductSpaces.angle_between_vectors import angle

a = [1, 5, 4]
b = [1, 3, 1]

print("The P2 inner product is", dot(a, b))
print("Angle between these is", angle(a, b, "degrees"))

'''
The following polynomials are orthogonal
r = x
s = x**2
'''
r = [0, 1, 0]
s = [0, 0, 1]
print("Orthogonal functions have {} as inner product".format(dot(r, s)))
print("Angle between these is", angle(r, s, "degrees"))