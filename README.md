# bhojanha_IA626-Project
# Real Estate Analysis with Per Capita Income of New York and Neighbouring States
# Reading CSV
Code:

import numpy as np

import pandas as pd

df = pd.read_csv("realtordata.csv")

df.head(950000)

Output: <img width="999" alt="final project-1" src="https://user-images.githubusercontent.com/54153457/207168190-58ab52dc-059a-4b94-a3ad-9422d52987d2.png">


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

Output: <img width="999" alt="final project - 2" src="https://user-images.githubusercontent.com/54153457/207178648-b2573469-2c24-480e-8580-d33b14719a49.png">


# Selecting Rows with Sold_Date

Code:

df2 = df.dropna(axis=0, subset=['sold_date'])

df2

Output: <img width="1003" alt="final project - 3" src="https://user-images.githubusercontent.com/54153457/207178756-4dad8311-9b8c-4b47-948d-5237b9d3d90c.png">


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

Output: <img width="1010" alt="final project - 4" src="https://user-images.githubusercontent.com/54153457/207178839-f6117452-6b96-4b7e-bf19-e99fa1a42069.png">


# Converting DataFrame to a new csv

Code:

merged.to_csv("merged.csv")

# Renaming Column zip_code to zip

Code:

merg = pd.read_csv('merged.csv')

merg = merg.rename(index = str,columns = {'zip_code':'zip'})
merg

Output: <img width="1010" alt="final project - 5" src="https://user-images.githubusercontent.com/54153457/207178898-dd869c2f-cf40-487c-879f-6c4b8d952ef3.png">

 
# Reading Income DataSet

Code:

income = pd.read_csv('Income.csv')

income

Output: 

https://user-images.githubusercontent.com/54153457/207168002-0cecf66d-731b-41da-bd08-c8b6a6a727bd.mov

# Reading a US zipcodes Dataset

Code:

zips = pd.read_csv('uszips.csv')

zips

Output: 

https://user-images.githubusercontent.com/54153457/207181221-da9a02e3-aa6a-4a50-8132-29c302e24987.mov



# Selecting data from New York and Neighbouring states

Code:

zips_NewYork2  = zips[zips['state_id'] =='NY']

zips_Vermont2 = zips[zips['state_id'] =='VT']

zips_Mass2 = zips[zips['state_id'] =='MA']

zips_NewHamp2 = zips[zips['state_id'] =='NH']

zips_Connect2 = zips[zips['state_id'] =='CT']

zips_Penn2 = zips[zips['state_id'] =='PA']

zips_RhodeIsland2 = zips[zips['state_id'] =='RI']

zips_NewJersey2 = zips[zips['state_id'] =='NJ']

zips2 = pd.concat([zips_NewYork2, zips_Vermont2, zips_Mass2, zips_NewHamp2, zips_Connect2, zips_Penn2, zips_RhodeIsland2, zips_NewJersey2])

zips2

Output: 

https://user-images.githubusercontent.com/54153457/207179316-2693e1e6-0a9a-4463-a3e3-01302493f172.mov



# Merging Income and zips datasets with a common column state_id

Code:

merged_df = zips2.merge(income, how = 'inner', on = ['state_id'])

merged_df

Output: 

https://user-images.githubusercontent.com/54153457/207179402-3e6d34d6-06fe-46b1-9993-cf4d895e15d8.mov



# Dropping all the duplicate zipcode values from the dataset

Code:

merged_df3=merged_df.drop_duplicates('zip')

merged_df3

Output: 

https://user-images.githubusercontent.com/54153457/207179439-7b7a3629-9e25-47b6-9835-b7f866c8d428.mov



# Dropping all the unnecessary rows from the dataset

Code:

merged_df3= merged_df.drop(['city','parent_zcta','zcta', 'population', 'density', 'county_fips','county_weights', 'county_names_all', 'county_fips_all', 'imprecise','military', 'timezone', 'GEOID', 'Deep_Pov_All', 'Deep_Pov_Children', 'NumAll_inPOV_ACS', 'PCTPOV017', 'POV017','POVALL', 'PCTPOVALL', 'Num_inPOV_0_17_ACS'], axis = 1)

# Merging the new dataset with the realtor dataset

Code:

final = pd.merge(merged_df3,merg,how = 'inner',on = 'zip')

final 

Output: 

https://user-images.githubusercontent.com/54153457/207179474-e4999cac-a3d1-45fe-8584-d1ed00b7a127.mov



# Dropping all the unnecessary columns from the final dataset 

Code: 

final2=final.drop(['county_fips','county_name','county_weights','county_names_all','county_fips_all','Num_inPOV_0_17_ACS','Unnamed:0','state_id','city_x','zcta','parent_zcta','density','city_y','state','Deep_Pov_All','Deep_Pov_Children','imprecise','military','timezone','GEOID','County','PCTPOVALL','Poverty_Rate_0_17_ACS','Poverty_Rate_ACS','NumAll_inPOV_ACS','PCTPOV017','POV017','Median_HH_Inc_ACS','POVALL'], axis = 1)

Output: 

https://user-images.githubusercontent.com/54153457/207179514-1e8a443b-a82f-4475-8807-6938080bd8f6.mov



# Finding Correlation between price and per capita income 

Code: 

print(final2['price'].corr(final2['PerCapitaInc']))

Output:  -0.030422948728633353

Code: 

print(final2.corr())

Output: 

https://user-images.githubusercontent.com/54153457/207179576-6629c368-ea23-41b9-b037-2f7d841ef91e.mov



# Plotting a correlation graph 

Code: 

import sklearn

import seaborn as sns

import matplotlib.pyplot as plt

correlation_data=final2.select_dtypes(include=[np.number]).corr()

mask = np.zeros_like(correlation_data, dtype=np.bool)

mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize=(11, 9))


cmap = sns.palette="vlag"

sns.heatmap(correlation_data, mask=mask, cmap=cmap, vmax=.3, center=0,

            square=True, linewidths=.5, cbar_kws={"shrink": .5});

Output: <img width="1012" alt="final project -14 " src="https://user-images.githubusercontent.com/54153457/207179624-90cf2243-1867-48ad-909a-b24e7c89cea4.png">


# Heatmap 

Code:

f,ax = plt.subplots(figsize=(15, 15))
sns.heatmap(final2.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()

Output: 

https://user-images.githubusercontent.com/54153457/207179675-a5ee5ecd-9b1b-4e48-bb7b-bc22e5926c78.mov



# Adding a new column price/PerCapitaInc

Code: 

final2['price,percapitainc'] = final2['price'] / final2['PerCapitaInc']
final2

Output: 

https://user-images.githubusercontent.com/54153457/207179728-2e1ae946-0971-4e57-aacb-837ac38e9338.mov

# Data Visualization using Power BI

1. Plotting Average price by per capita income using line graph
![h1](https://user-images.githubusercontent.com/54153457/207184235-406ebc5d-5dc2-4ffb-ad20-7c6e680738b9.jpeg)



2. Plotting of Average Per Capita Income and Average Price by Zipcodes using Area Chart
![h2](https://user-images.githubusercontent.com/54153457/207184438-083ab327-4ff7-4b43-b826-b3bb12bea729.jpeg)



            
3. Plotting average Pirce and Average Per Capita Income by State using Clustered Column Chart
![h3](https://user-images.githubusercontent.com/54153457/207184466-15b11ba4-1d71-4582-af7d-a8c83944fcf1.jpeg)




4. Plotting Average House Size and Average Price by State using Area Chart
![h4](https://user-images.githubusercontent.com/54153457/207184483-621ce85d-dd4a-4680-a8b3-91a9652c4690.jpeg)




