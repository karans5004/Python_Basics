'''
Python is not “statically typed”. We do not need to declare variables before using them or declare their type. A variable is created the moment we first assign a value to it. A variable is a name given to a memory location. It is the basic unit of storage in a program.

    The value stored in a variable can be changed during program execution.
    A variable is only a name given to a memory location, all the operations done on the variable effects that memory location.

Rules for creating variables in Python:

    A variable name must start with a letter or the underscore character.
    A variable name cannot start with a number.
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
    Variable names are case-sensitive (name, Name and NAME are three different variables).
    The reserved words(keywords) cannot be used naming the variable.

'''
######################################################
# An integer assignment
age = 45
  
# A floating point
salary = 1456.8
  
# A string
name = "John"
  
print(age)
print(salary)
print(name)
##########################################################


########################################################
# declaring the var
Number = 100
  
# display
print("Before declare: ", Number)
  
# re-declare the var
Number = 120.3
    
print("After re-declare:", Number)
#########################################################

####################################################### Single valu to multiple variables
a = b = c = 10
  
print(a)
print(b)
print(c)
##########################################################

############################################################3
a, b, c = 1, 20.2, "GeeksforGeeks"
  
print(a)
print(b)
print(c)
###########################################################

#############################################################3
a = 10
a = "GeeksforGeeks"
  
print(a)
###########################################################

################33Local#####################3333

def f():
    s = "Welcome geeks"
    print(s)
  
  
f()

################################################33

##################################################3

# This function has a variable with
# name same as s.
def f():
    print(s)
  
  
# Global scope
s = "I love Geeksforgeeks"
f()

########################################

""" Global keyword in Python:

Global keyword is a keyword that allows a user to modify a variable outside of the current scope. It is used to create global variables from a non-global scope i.e inside a function. Global keyword is used inside a function only when we want to do assignments or when we want to change a variable. Global is not needed for printing and accessing.

Rules of global keyword:

    If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.
    Variables that are only referenced inside a function are implicitly global.
    We Use global keyword to use a global variable inside a function.
    There is no need to use global keyword outside a function. """

""" # Python program to modify a global
# value inside a function
  
x = 15
  
  
def change():
  
    # using a global keyword
    global x
  
    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)
  
  
change()
print("Value of x outside a function :", x) """