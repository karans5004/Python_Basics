""" 1. ceil() :- This function returns the smallest integral value greater than the number. If number is already integer, same number is returned.
2. floor() :- This function returns the greatest integral value smaller than the number. If number is already integer, same number is returned.
3. fabs() :- This function returns the absolute value of the number.
4. factorial() :- This function returns the factorial of the number. An error message is displayed if number is not integral.
5. copysign(a, b) :- This function returns the number with the value of âaâ but with the sign of âbâ. The returned value is float type.

6. gcd() :- This function is used to compute the greatest common divisor of 2 numbers mentioned in its arguments. This function works in python 3.5 and above.
 """
""" # Python code to demonstrate the working of
# ceil() and floor()
  
# importing "math" for mathematical operations
import math
  
a = 2.3
  
# returning the ceil of 2.3
print ("The ceil of 2.3 is : ", end="")
print (math.ceil(a))
  
# returning the floor of 2.3
print ("The floor of 2.3 is : ", end="")
print (math.floor(a))
 """





""" # Python code to demonstrate the working of
# fabs() and factorial()
  
# importing "math" for mathematical operations
import math
  
a = -10
  
b= 5
  
# returning the absolute value.
print ("The absolute value of -10 is : ", end="")
print (math.fabs(a))
  
# returning the factorial of 5
print ("The factorial of 5 is : ", end="")
print (math.factorial(b))
 """




# Python code to demonstrate the working of
# copysign() and gcd()
"""   
# importing "math" for mathematical operations
import math
  
a = -10
b = 5.5
c = 15
d = 5
  
# returning the copysigned value.
print ("The copysigned value of -10 and 5.5 is : ", end="")
print (math.copysign(5.5, -10))
  
# returning the gcd of 15 and 5
print ("The gcd of 5 and 15 is : ", end="")
print (math.gcd(5,15)) """