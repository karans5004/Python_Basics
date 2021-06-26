a_list = [86,86,85,85,85,83,23,45,84,1,2,0]
 
# method 1
 
def second_best(a):
    if a:
 
        first = a[0]
 
        second = None
 
        for i in range(1,len(a)):
 
            if second == None or second == first:
 
                second = a[i]
 
            if second < a[i]:
 
                second = a[i]
 
            if second > first:
 
                first, second = second, first
 
        return first, second
 
    else:
 
        return None, None
 
#function called     
 
f,s  = second_best(a_list)
 
print("First : {0} Second : {1}".format(f,s))
 
 
 
#method 2
 
#sort the list and get the elements
 
a_list = [84,84,86,86,85,85,85,83,23,45,84,1,2,0]
 
def first_second(given_list):
 
    a = given_list   #make a copy
 
    a.sort(reverse=True)
 
    print(a)
 
    first = a[0]
 
    second = None
 
    for element in a_list:
 
        if element != first:
 
            second = element
 
            return first, second
 
#function called
 
f,s = first_second(a_list)
 
print(f,s)