# Python3 Program to check whether a 
# given key already exists in a dictionary.
  
# Function to print sum
def checkKey(dict, key):
      
    if key in dict.keys():
        return 1
    else:
        return 0
  
# Driver Code
dict = {'a': 100, 'b':200, 'c':300}
  
key = input('Please Enter the Key : ')
flag = checkKey(dict, key)

if(flag == 1):
    print("Value for given key is : " ,dict[key])
    #print its val
else:
    new_value = input('Please enter a value for key')
    dict[key] = new_value
    #add the new key to the dictionary

#fincal dictionary
print("final Dictionary is : ", dict)