# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 23:05:38 2022

@author: jerryavance
"""

"""
Example of a trace

Consider the following Python program that computes 
a sum of squares of successive whole numbers until that 
sum exceeds 100000:
"""   
def square(x):
    return x * x

i = 0
y = 0
while True:
    y += square(i)
    if y > 100000:
        break
    i = i + 1
    
#A trace for this program could look something like this:

loopstart(i1, y1)
 i2 = int_mul(i1, i1)		# x*x
 y2 = int_add(y1, i2)		# y += i*i
 b1 = int_gt(y2, 100000)
 guard_false(b1)
 i3 = int_add(i1, 1)		# i = i+1
 jump(i3, y2)
 
#Note how the function call to square is inlined into the trace and how the if statement is turned into a guard_false
