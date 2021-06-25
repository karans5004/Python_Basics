""" In Python, anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions. It has the following syntax:

Syntax

lambda arguments : expression

    This function can have any number of arguments but only one expression, which is evaluated and returned.
    One is free to use lambda functions wherever function objects are required.
    You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
    It has various uses in particular fields of programming besides other types of expressions in functions. """


"""     # Python program to demonstrate
# lambda functions
  
  
x ="GeeksforGeeks"
  
# lambda gets pass to print 
(lambda x : print(x))(x) """


""" # Python program to illustrate cube of a number  
# showing difference between def() and lambda().
  
  
def cube(y): 
    return y*y*y; 
    
g = lambda x: x*x*x 
print(g(7)) 
    
print(cube(5)) """


#Illustration from when inside a function
""" # Python program to demonstrate
# lmabda functions
  
  
def power(n):
    return lambda a : a ** n
  
# base = lambda a : a**2 get 
# returned to base
base = power(2)
  
print("Now power is set to 2")
  
# when calling base it gets 
# executed with already set with 2
print("8 powerof 2 = ", base(8))
  
# base = lambda a : a**5 get 
# returned to base
base = power(5)
print("Now power is set to 5")
  
# when calling base it gets executed
# with already set with newly 2
print("8 powerof 5 = ", base(8)) """


#filter and map
""" 
# Python program to demonstrate
# lambda functions inside map()
# and filter()
  
  
a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]
  
# in filter either we use assignment or 
# conditional operator, the pass actual 
# parameter will get return
filtered = filter (lambda x: x % 2 == 0, a) 
print(list(filtered))
  
# in map either we use assignment or
# conditional operator, the result of 
# the value will get returned
maped = map (lambda x: x % 2 == 0, a) 
print(list(maped)) """