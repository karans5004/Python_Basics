# Python program to illustrate
# while loop
""" count = 0
while (count < 3):   
    count = count + 1
    print("Hello Geek") """


#while Else

""" #Python program to illustrate
# combining else with while
count = 0
while (count < 3):   
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block") """

#single statement while block

""" # Python program to illustrate
# Single statement while block
count = 0
while (count == 0): print("Hello Geek") """

#for in loop
""" 
# Python program to illustrate
# Iterating over range 0 to n-1
 
n = 4
for i in range(0, n):
    print(i) """

#Iterations

""" # Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
      
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
      
# Iterating over a String
print("\nString Iteration")   
s = "Geeks"
for i in s :
    print(i)
      
# Iterating over dictionary
print("\nDictionary Iteration")  
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i])) """

#forelse

""" # Python program to illustrate
# combining else with for
 
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print list[index]
else:
    print "Inside Else Block" """

#continue
"""     # Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
         continue
    print('Current Letter :', letter)
    var = 10 """

#break

""" for letter in 'geeksforgeeks':
 
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
         break
 
print 'Current Letter :', letter """