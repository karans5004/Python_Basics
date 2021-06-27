""" # Python program for
# Creation of Arrays
import numpy as np
 
# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n",arr)
 
# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)
 
# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr) """

#Indexed Array

""" # Python program to demonstrate
# indexing in numpy array
import numpy as np
 
# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)
 
# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)
 
# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr) """

#Basic Array Operations

""" # Python program to demonstrate
# basic operations on single array
import numpy as np
 
# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
# Adding 1 to every element
print ("Adding 1 to every element:", a + 1)
 
# Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)
 
# sum of array elements
# Performing Unary operations
print ("\nSum of all array "
       "elements: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray sum:\n", a + b) """

#constructing a Datatype object

""" # Python Program to create
# a data type object
import numpy as np
 
# Integer datatype
# guessed by Numpy
x = np.array([1, 2])  
print("Integer Datatype: ")
print(x.dtype)         
 
# Float datatype
# guessed by Numpy
x = np.array([1.0, 2.0]) 
print("\nFloat Datatype: ")
print(x.dtype)  
 
# Forced Datatype
x = np.array([1, 2], dtype = np.int64)   
print("\nForcing a Datatype: ")
print(x.dtype) """

#Math Operations on DataType Array

""" # Python Program to create
# a data type object
import numpy as np
 
# First Array
arr1 = np.array([[4, 7], [2, 6]], 
                 dtype = np.float64)
                  
# Second Array
arr2 = np.array([[3, 6], [2, 8]], 
                 dtype = np.float64) 
 
# Addition of two Arrays
Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)
 
# Addition of all Array elements
# using predefined sum method
Sum1 = np.sum(arr1)
print("\nAddition of Array elements: ")
print(Sum1)
 
# Square root of Array
Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)
 
# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr) """

# Array Transposition

""" # importing python module named numpy
import numpy as np
  
# making a 3x3 array
gfg = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
  
# before transpose
print(gfg, end ='\n\n')
  
# after transpose
print(gfg.transpose()) """

# Universal Array Function

#Trignometric

""" # Python code to demonstrate trignometric function
import numpy as np
  
# create an array of angles
angles = np.array([0, 30, 45, 60, 90, 180]) 
  
# conversion of degree into radians
# using deg2rad function
radians = np.deg2rad(angles)
  
# sine of angles
print('Sine of angles in the array:')
sine_value = np.sin(radians)
print(np.sin(radians))
  
# inverse sine of sine values
print('Inverse Sine of sine values:')
print(np.rad2deg(np.arcsin(sine_value)))
  
# hyperbolic sine of angles
print('Sine hyperbolic of angles in the array:')
sineh_value = np.sinh(radians)
print(np.sinh(radians))
  
# inverse sine hyperbolic 
print('Inverse Sine hyperbolic:')
print(np.sin(sineh_value)) 
  
# hypot function demonstration
base = 4
height = 3
print('hypotenuse of right triangle is:')
print(np.hypot(base, height)) """

# Statistical Function

""" # Python code demonstrate statistical function
import numpy as np
  
# construct a weight array
weight = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45])
  
# minimum and maximum 
print('Minimum and maximum weight of the students: ')
print(np.amin(weight), np.amax(weight))
  
# range of weight i.e. max weight-min weight
print('Range of the weight of the students: ')
print(np.ptp(weight))
  
# percentile
print('Weight below which 70 % student fall: ')
print(np.percentile(weight, 70))
   
# mean 
print('Mean weight of the students: ')
print(np.mean(weight))
  
# median 
print('Median weight of the students: ')
print(np.median(weight))
  
# standard deviation 
print('Standard deviation of weight of the students: ')
print(np.std(weight))
  
# variance 
print('Variance of weight of the students: ')
print(np.var(weight))
  
# average 
print('Average weight of the students: ')
print(np.average(weight)) """

# Bit Twidling Functions

""" # Python code to demonstrate bitwise-function
import numpy as np
  
# construct an array of even and odd numbers
even = np.array([0, 2, 4, 6, 8, 16, 32])
odd = np.array([1, 3, 5, 7, 9, 17, 33])
  
# bitwise_and
print('bitwise_and of two arrays: ')
print(np.bitwise_and(even, odd))
  
# bitwise_or
print('bitwise_or of two arrays: ')
print(np.bitwise_or(even, odd))
  
# bitwise_xor
print('bitwise_xor of two arrays: ')
print(np.bitwise_xor(even, odd))
   
# invert or not
print('inversion of even no. array: ')
print(np.invert(even))
  
# left_shift 
print('left_shift of even no. array: ')
print(np.left_shift(even, 1))
  
# right_shift 
print('right_shift of even no. array: ')
print(np.right_shift(even, 1)) """


# Multidimentional Input Array Processing

""" import numpy as np
  
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix) """

# Same Multidimentional input array without numpy

""" # A basic code for matrix input from user
  
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print() """