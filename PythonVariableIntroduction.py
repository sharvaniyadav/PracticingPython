# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:38:34 2024

@author: Sharvani Yadav
"""
"Python Variables Elaboration:"

#----------------------------------------------------------------------------------------------------------------------------------------------

# Creating Variable:

x = 5       # A variable is created the moment I first assign a value to it
y = "John"
print(x)    # Prints the variable value
print(y)    # Prints the variable value

# Variables do not need to be declared with any particular type, and can even change type after they have been set
x = 4       # x is of type int
x = "Sally" # x is NOW of type str
print(x)    # Code will print the most recent variable value of x depending on variable type
            # If I added x = "Mandy" right after line 17, it would print the most recent 
            # value assigned to the variable x for that particular variable type
            # ???

#----------------------------------------------------------------------------------------------------------------------------------------------

# Casting Varaibles:
"To specify the data type of a variable, this can be done with casting"

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#----------------------------------------------------------------------------------------------------------------------------------------------

# Get the Type:
"Get the data type of a variable with the type() function"

x = 5
y = "John"
print(type(x)) # Basically tells what type of variable it is. In this case 5 is an int variable
print(type(y)) # Basically tells what type of variable it is. In this case John is an string variable

#----------------------------------------------------------------------------------------------------------------------------------------------

# String variables can be declared either by using single or double quotes:
"Single or Double Quotes?"

x = "John"
# is the same as
x = 'John'
print(x)

#----------------------------------------------------------------------------------------------------------------------------------------------

# Case Sensitve - Variables are case sensitive:
"This will create two variables:"

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

























