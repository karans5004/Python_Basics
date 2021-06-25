
#https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/

""" # A simple Python function to check
# whether x is even or odd
 
 
def evenOdd(x):
    if (x % 2 == 0):
        print "even"
    else:
        print "odd"
 
 
# Driver code to call the function
evenOdd(2)
evenOdd(3) """

""" def say_Hi():
    "Hello! geeks!"
 
 
print(say_Hi.__doc__)
 """


""" def square_value(num):
    '''This function returns the square
    value of the entered number'''
    return num**2
 
 
print(square_value(2))
 
print(square_value(-4)) """

""" Pass by Reference or pass by value? 

One important thing to note is, in Python every variable name is a reference. 
When we pass a variable to a function, a new reference to the object is created. 
Parameter passing in Python is the same as reference passing in Java. """

""" # Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20
 
 
# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst) """

""" def myFun(x):
 
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]
 
 
# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst) """

""" def myFun(x):
 
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20
 
 
# Driver Code (Note that lst is not modified
# after function call.
x = 10
myFun(x)
print(x) """

""" def swap(x, y):  GUESSthe output of this code
    temp = x
    x = y
    y = temp
 
 
# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y) """

""" # Python program to demonstrate
# default arguments
 
 
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
 
 
# Driver code (We call myFun() with only
# argument)
myFun(10) """

""" # Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
 
 
# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks') """


