# import the required packages 
import pandas as pd 
  
# Define the dictionary for converting to dataframe 
movies = {'Name': ['The Godfather', 'Bird Box', 'Fight Club'],
         'Year': ['1972', '2018', '1999'],
         'Rating': ['9.2', '6.8', '8.8']}
  
df = pd.DataFrame(movies)
print(df)

# Create a column Rating_Rank which contains
# the rank of each movie based on rating
df['Rating_Rank'] = df['Rating'].rank(ascending = 1)
  
# Set the index to newly created column, Rating_Rank
df = df.set_index('Rating_Rank')
print(df)

# Sort the dataFrame based on the index
df = df.sort_index()
print(df)