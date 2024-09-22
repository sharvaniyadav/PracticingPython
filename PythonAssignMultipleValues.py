# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:07:59 2024

@author: Sharvani Yadav
"""

"Python Variables - Assign Multiple Value"

#---------------------------------------------------------------------------------------------------------------------------

"Many Values to Multiple Variables"
# Python allows you to assign values to multiple variables in one line:
    
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

"One Value to Multiple Variables"
# Can assign the same value to multiple variables in one line:
    
x = y = z = "Orange"
print(x)
print(y)
print(z)

"Unpack a Collection"
# If I have a collection of values in a list, tuple etc. 
# Python allows me to extract the values into variables. 
# This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits 
# line 34 and line 35 are the SAME command!
fruits = x, y, z
print(x)
print(y)
print(z)
