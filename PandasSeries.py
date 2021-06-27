# Series from Array
""" # import pandas as pd
import pandas as pd
 
# import numpy as np
import numpy as np
 
# simple array
data = np.array(['g','e','e','k','s'])
 
ser = pd.Series(data)
print(ser) """


#Series from Lists

""" import pandas as pd
 
# a simple list
list = ['g', 'e', 'e', 'k', 's']
  
# create series form a list
ser = pd.Series(list)
print(ser) """


#Accessing Elements from Series

""" # import pandas and numpy 
import pandas as pd
import numpy as np
 
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data)
  
  
#retrieve the first 5 elements
print(ser[:5]) """


#Position Accessing
""" 
# import pandas and numpy 
import pandas as pd
import numpy as np
 
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
  
  
# accessing a element using index element
print(ser[16]) """


#From CSV file with indexes
""" # importing pandas module  
import pandas as pd  
     
# making data frame  
df = pd.read_csv("as.csv")  
   
ser = pd.Series(df['fname']) 
data = ser.head(10)
data 

print(data[3:6])  """

#From CSV using loc

""" # importing pandas module  
import pandas as pd  
     
# making data frame  
df = pd.read_csv("as.csv")  
   
ser = pd.Series(df['fname']) 
data = ser.head(10)
data 
print(data.loc[3:6]) """


#Run the following in juptyer
""" # Python code demonstrate creating 
# DataFrame from dict and left aligning
import pandas as pd 
  
# intialise data of lists. 
data = {'Name' : ['Tania', 'Ravi', 
                  'Surbhi', 'Ganesh'], 
          
        'Articles' : [50, 30, 45, 33], 
          
        'Location' : ['Kanpur', 'Kolkata',
                      'Kolkata', 'Bombay']} 
  
# Create DataFrame 
df = pd.DataFrame(data) 
  
left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
display(left_aligned_df) """