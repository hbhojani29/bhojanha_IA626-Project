# bhojanha_IA626-Project
# Real Estate Analysis with Per Capita Income of New York and Neighbouring States
# Reading CSV
Code:

import numpy as np

import pandas as pd

df = pd.read_csv("realtordata.csv")

df.head(950000)

Output: 1

# Removing Null Values

Code:

df1 = df.dropna(axis = 0,  how ='any') 

df1

print("Number of rows with at least 1 NA value: ",
      (len(df)-len(df1)))
      
->  Number of rows with at least 1 NA value:  691172

print("New data frame length:", len(df1))

-> New data frame length: 231987

print("Old data frame length:", len(df)) 

-> Old data frame length: 923159

Output: 2

# Selecting Rows with Sold_Date

Code:

df2 = df.dropna(axis=0, subset=['sold_date'])

df2

Output: 3

# Selecting data from New York and Neighbouring states

Code:

df_NewYork = df2[df2['state'] =='New York']

df_Vermont = df2[df2['state'] =='Vermont']

df_Mass = df2[df2['state'] =='Massachusetts']

df_NewHamp = df2[df2['state'] =='New Hampshire']

df_Connect = df2[df2['state'] =='Connecticut']

df_Penn = df2[df2['state'] =='Pennsylvania']

df_RhodeIsland = df2[df2['state'] =='Rhode Island']

df_NewJersey = df2[df2['state'] =='New Jersey']

merged = pd.concat([df_NewYork, df_Vermont, df_Mass, df_NewHamp, df_Connect, df_Penn, df_RhodeIsland, df_NewJersey])

merged

Output: 4

# Converting DataFrame to a new csv

Code:

merged.to_csv("merged.csv")

# Renaming Column zip_code to zip

Code:

merg = pd.read_csv('merged.csv')

merg = merg.rename(index = str,columns = {'zip_code':'zip'})
merg

Output: 5
 
# Reading Income DataSet

Code:

income = pd.read_csv('Income.csv')

income

Output: [![Alternate Text]({image-url})]({video-url} "Link Title")



