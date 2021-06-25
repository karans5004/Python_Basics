""" # Python Program to 
# show range() basics
  
# printing a number
for i in range(10):
    print(i, end =" ")
print()
  
# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end =" ")
print()
  
# performing sum of natural
# number
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum of first 10 natural number :", sum)
 """



#start stop step
""" 
# Python program to 
# print all number 
# divisible by 3 and 5
   
# using range to print number
# divisible by 3
for i in range(0, 30, 3):
    print(i, end = " ")
print()
  
# using range to print number
# divisible by 5
for  i in range(0, 50, 5):
     print(i, end = " ") """

"""      Points to remember about Python range() function :

    range() function only works with the integers i.e. whole numbers.
    All argument must be integers. User can not pass a string or float number or any other type in a start, stop and step argument of a range().
    All three arguments can be positive or negative.
    The step value must not be zero. If a step is zero python raises a ValueError exception.
    range() is a type in Python """