""" # Creating non-empty tuples
  
# One way of creation
tup = 'python', 'geeks'
print(tup)
  
# Another for doing the same
tup = ('python', 'geeks')
print(tup)
 """

#concatination
""" 
# Code for concatenating 2 tuples
  
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
  
# Concatenating above two
print(tuple1 + tuple2) """

#Nesting
""" 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3) """

#repition
""" 
tuple3 = ('python',)*3
print(tuple3) """

#immutable example

""" #code to test that tuples are immutable
  
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1) """

#slicing

""" # code to test slicing
  
tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4]) """

#length
""" # Code for printing the length of a tuple
  
tuple2 = ('python', 'geek')
print(len(tuple2)) """

#convert list to tuple
""" 
# Code for converting a list and a string into a tuple
  
list1 = [0, 1, 2]
print(tuple(list1))
print(tuple('python')) # string 'python' """

#tuples in loop

""" #python code for creating tuples in a loop
  
tup = ('geek',)
n = 5  #Number of time loop runs
for i in range(int(n)):
    tup = (tup,)
    print(tup) """

