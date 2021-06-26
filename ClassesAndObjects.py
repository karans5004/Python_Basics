""" # Python3 program to
# demonstrate instantiating
# a class
 
 
class Dog:
     
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method 
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
 
# Driver code
# Object instantiation
Rodger = Dog()
 
# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun() """


# Self And Init

""" # A Sample class with init method
class Person:
   
    # init method or constructor 
    def __init__(self, name):
        self.name = name
   
    # Sample Method 
    def say_hi(self):
        print('Hello, my name is', self.name)
   
p = Person('Nikhil')
p.say_hi() """

# Classes and Instance Variables

# Python3 program to show that the variables with a value 
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
    
# Class for Dog

""" class Dog:
   
    # Class Variable
    animal = 'dog'            
   
    # The init method or constructor
    def __init__(self, breed, color):
     
        # Instance Variable    
        self.breed = breed
        self.color = color       
    
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
 
print('Rodger details:')  
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
 
print('\nBuzo details:')  
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
 
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)   """


# Accessing Attributes and Methods

""" # Python code for Accessing attributes and methods 
# of one class in another class 
  
class ClassA(): 
    def __init__(self): 
        self.var1 = 1
        self.var2 = 2
  
    def methodA(self): 
        self.var1 = self.var1 + self.var2 
        return self.var1 
  
class ClassB(ClassA): 
    def __init__(self, class_a): 
        self.var1 = class_a.var1 
        self.var2 = class_a.var2 
  
object1 = ClassA() 
# updates the value of var1 
summ = object1.methodA() 
  
# return the value of var1 
print (summ) 
  
# passes object of classA 
object2 = ClassB(object1) 
  
# return the values carried by var1,var2 
print( object2.var1)
print (object2.var2)  """