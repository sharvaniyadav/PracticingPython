# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:18:03 2024

@author: Sharvani Yadav
"""

"Python Output Variables"

"Output Variables: The Python print() function is often used to output variables."
x = "Python is awesome"
print(x)

"In the print() function, you output multiple variables, separated by a comma:"
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

"Also use the + operator to output multiple variables:"
x = "Python " # When using plus function from line 24, make sure to add space after word
y = "is "     # otherwise it will produce the output "Pythonisawesome" with NO spaces
z = "awesome"
print(x + y + z)

"NOTE: For numbers, the + character works as a mathematical operator:"
x = 5
y = 10
print(x + y) # Output will be 15.

""""
IMPORTANT NOTE: When using + operator, only work with same varaible type
    So it will NOT work when I do:
    x = 5
    y = "John"
    print(x + y)
    
    Output will give ERROR.
    This is because x is int & y is string variable

    INSTEAD DO THIS, separate them with commas, which even support different data types
"""
# Below this is how to print variables of different data types:
x = 5
y = "John"
print(x, y)



























