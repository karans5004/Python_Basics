""" ########################## Use of and or not true false Keyword #####################################
print("example of True, False, and, or not keywords")

#  compare two operands using and operator
print(True and True)
 
# compare two operands using or operator
print(True or False)
 
# use of not operator
print(not False)
##################################################################################### 
  """



""" ########################## Use of break continue Keyword #####################################
# execute for loop
for i in range(1, 11):
     
    # print the value of i
    print(i)
     
    # check the value of i is less then 5
    # if i lessthen 5 then continue loop
    if i < 5: 
        continue
         
    # if i greather then 5 then break loop
    else: 
        break
#####################################################################################
 """




""" ########################## Use of for in if elif Keyword #####################################

# run for loop
for t in range(1, 5):
  # print one of t ==1
    if t == 1:
        print('One')
   # print two if t ==2
    elif t == 2:
        print('Two')
    else:
        print('else block execute')
#####################################################################################
 """


""" 
########################## Use of def if else Keyword #####################################
# define GFG() function using def keyword
def GFG():
    i=20
    # check i is odd or not
    # using if and else keyword
    if(i % 2 == 0):
        print("given number is even")
    else:
        print("given number is odd")   
     
# call GFG() function   
GFG()
#####################################################################################
 """



""" ########################## Use of try except raise Keyword #####################################
def fun(num):
    try:
        r = 1/num
    except:
        print('Exception raies')
        return
    return r
 
print(fun(10))
print(fun(0))
#####################################################################################
 """



""" ########################## Use of return Keyword #####################################
# define a anonymous using lambda keyword
# this labda function increment the value of b
a = lambda b: b+1
 
# run a for loop
for i in range(1, 6):
    print(a(i))
#####################################################################################
 """


 

""" ########################## Use of return Keyword #####################################

# define a function
def fun():
  # declare a variable
    a = 5
    # return the value of a
    return a
# call fun method and store
# it's return value in a variable 
t = fun()
# print the value of t
print(t)
#####################################################################################
 """






""" ########################## Use of del Keyword #####################################

# create a list
l = ['a', 'b', 'c', 'd', 'e']
 
# print list before using del keyword
print(l)
 
del l[2]
 
# print list after using del keyword
print(l)
#####################################################################################
 """




""" ########################## Use of global Keyword #####################################

# declare a variable
gvar = 10
 
# create a function
def fun1():
  # print the value of gvar
    print(gvar)
 
# declare fun2()
def fun2():
  # declare global value gvar
    global gvar
    gvar = 100
 
# call fun1()
fun1()
 
# call fun2()
fun2()
#####################################################################################
 """




""" 
########################## Use of yield Keyword #####################################

def Generator():
    for i in range(6):
        yield i+1
 
t = Generator()
for i in t:
    print(i)
#####################################################################################

 """




""" ########################## Use of Assert Keyword #####################################

def sumOfMoney(money):
    assert len(money) != 0,"List is empty."
    return sum(money)
 
money = []
print("sum of money:",sumOfMoney(money))

#####################################################################################
 """




"""
Identifiers: The identifier is a name used to identify a variable, function, class, module, etc. The identifier is a combination of character digits and underscore. 
The identifier should start with a character or Underscore then use digit. The characters are A-Z or a-z,a UnderScore ( _ ) and digit (0-9). we should not use special characters ( #, @, $, %, ! ) in identifiers.

Examples of valid identifiers:

    var1
    _var1
    _1_var
    var_1

Examples of invalid identifiers

    !var1
    1var
    1_var
    var#1
"""