# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:05:33 2024

@author: Sharvani Yadav
"""

"Python - Globral Variables"

"""
Global variables are variables that are defined outside of any
function and are accessible throughout the entire program, 
including within functions. 

They have a global scope, meaning that once a global variable is declared, 
it can be used anywhere in the code, as long as the program hasn't exited.
"""

x = "awesome"  # Defining the Global variable

def myfunc():
    print(x)  # You can access the global variable inside this function
    print("Python is " +x)

myfunc() #this will print "awesome" and "Python is awesome"

# myfunc() and my_function() can be used interchangably!

x = "awesome"

def myfunc():  #variable with the same name was created hence it will be local and only used in this given function
  x = "fantastic"
  print("Python is " + x) # hence in this case the output will be "Python is fantastic" for this particular local variable in this function

myfunc()


print("Python is " + x) # This will print the originally defined global variable

"Global Keyword:"
print("Global Keyword Output:")

# use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, 
# refer to the variable by using the global keyword

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


























