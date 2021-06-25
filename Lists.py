# Python program to demonstrate
# Creation of List
"""  
# Creating a List
List = []
print("Blank List: ")
print(List)
 
# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
 
# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])
 
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'] , ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)


# Creating a List
List1 = []
print(len(List1))
 
# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))

 """

#append
""" 
# Python program to demonstrate
# Addition of elements in a List
 
# Creating a List
List = []
print("Initial blank List: ")
print(List)
 
# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)
 
# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
 
# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)
 
# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List) """


""" #insert
# Python program to demonstrate
# Addition of elements in a List
  
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)
 
# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List) """

#extend
""" 
 Python program to demonstrate
# Addition of elements in a List
   
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)
 
# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List) """


#access

""" # Python program to demonstrate
# accessing of element from list
 
# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
 
# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])
 
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'] , ['Geeks']]
 
# accessing an element from the
# Multi-Dimensional List using
# index number
print("Acessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0]) """


#Negative Indexing

""" List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
 
# accessing a element using
# negative indexing
print("Accessing element using negative indexing")
 
# print the last element of list
print(List[-1])
 
# print the third last element of list
print(List[-3]) """


#remove

""" # Python program to demonstrate
# Removal of elements in a List
 
# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
 
# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)
 
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List) """

#pop

""" List = [1,2,3,4,5]
 
# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)
 
# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List) """

#slicing

""" # Python program to demonstrate
# Removal of elements in a List
 
# Creating a List
List = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
print("Initial List: ")
print(List)
 
# Print elements of a range
# using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)
 
# Print elements from a
# pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)
 
# Printing elements from
# beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List) """