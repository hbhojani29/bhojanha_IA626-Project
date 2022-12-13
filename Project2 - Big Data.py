#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
df = pd.read_csv("realtordata.csv")
df.head(950000)


# In[3]:


df['sold_date'].value_counts()[:950000]


# In[89]:


df1 = df.dropna(axis = 0,  how ='any') 


# In[90]:


df1


# In[6]:


print("Number of rows with at least 1 NA value: ",
      (len(df)-len(df1)))


# In[7]:


print("New data frame length:", len(df1))


# In[8]:


print("Old data frame length:", len(df)) 


# In[9]:





# In[10]:


df2


# In[11]:


df_NewYork = df2[df2['state'] =='New York']
df_Vermont = df2[df2['state'] =='Vermont']
df_Mass = df2[df2['state'] =='Massachusetts']
df_NewHamp = df2[df2['state'] =='New Hampshire']
df_Connect = df2[df2['state'] =='Connecticut']
df_Penn = df2[df2['state'] =='Pennsylvania']
df_RhodeIsland = df2[df2['state'] =='Rhode Island']
df_NewJersey = df2[df2['state'] =='New Jersey']



# In[12]:


merged = pd.concat([df_NewYork, df_Vermont, df_Mass, df_NewHamp, df_Connect, df_Penn, df_RhodeIsland, df_NewJersey])


# In[13]:


merged


# In[14]:


#merged.to_csv("merged.csv")


# In[15]:


from geopy.geocoders import Nominatim


# In[16]:


###import requests
import urllib.parse

#address = 'Shivaji Nagar, Bangalore, KA 560001'
#url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

#response = requests.get(url).json()
#print(response[0]["lat"])
#print(response[0]["lon"])


# In[17]:


#n=0
#for i in merged['full_address']:
 #   url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(i) +'?format=json'
  #  response = requests.get(url).json()
   # print(response[0]["lat"])
    #print(response[0]["lon"])
   # if n==20:
  #      break
   # n+=1


# In[18]:


merg = pd.read_csv('merged.csv')


# In[19]:


merg = merg.rename(index = str,columns = {'zip_code':'zip'})
merg


# In[20]:


income = pd.read_csv('Income.csv')


# In[94]:


income


# In[22]:


zips = pd.read_csv('uszips.csv')


# In[23]:


zips


# In[24]:


#countyzip = pd.merge(income, zips, left_on="County", right_on="county_name")


# In[25]:


#countyzip


# In[26]:


zips_NewYork2  = zips[zips['state_id'] =='NY']
zips_Vermont2 = zips[zips['state_id'] =='VT']
zips_Mass2 = zips[zips['state_id'] =='MA']
zips_NewHamp2 = zips[zips['state_id'] =='NH']
zips_Connect2 = zips[zips['state_id'] =='CT']
zips_Penn2 = zips[zips['state_id'] =='PA']
zips_RhodeIsland2 = zips[zips['state_id'] =='RI']
zips_NewJersey2 = zips[zips['state_id'] =='NJ']

zips2 = pd.concat([zips_NewYork2, zips_Vermont2, zips_Mass2, zips_NewHamp2, zips_Connect2, zips_Penn2, zips_RhodeIsland2, zips_NewJersey2])


# In[27]:


zips2


# In[28]:


income = income.rename(index = str,columns = {'State':'state_id'})


# In[29]:


income


# In[30]:


merged_df = zips2.merge(income, how = 'inner', on = ['state_id'])


# In[31]:


merged_df


# In[59]:


merged_df3= merged_df.drop(['city','parent_zcta','zcta', 'population', 'density', 'county_fips','county_weights', 'county_names_all', 'county_fips_all', 'imprecise',
       'military', 'timezone', 'GEOID', 'Deep_Pov_All', 'Deep_Pov_Children', 'NumAll_inPOV_ACS', 'PCTPOV017',
       'POV017','POVALL', 'PCTPOVALL', 'Num_inPOV_0_17_ACS'], axis = 1)


# In[60]:


merged_df3=merged_df.drop_duplicates('zip')
merged_df3


# In[61]:


final = pd.merge(merged_df3,merg,how = 'inner',on = 'zip')


# In[62]:


final


# In[63]:


final2= final.drop(['Unnamed: 0','state_id','city_x','zcta','parent_zcta','density','city_y','state','Deep_Pov_All','Deep_Pov_Children'], axis = 1)


# In[64]:


final2


# In[78]:


final2= final.drop(['county_fips','county_name','county_weights','county_names_all','county_fips_all','Num_inPOV_0_17_ACS','Unnamed: 0','state_id','city_x','zcta','parent_zcta','density','city_y','state','Deep_Pov_All','Deep_Pov_Children','imprecise','military','timezone','GEOID','County','PCTPOVALL','Poverty_Rate_0_17_ACS','Poverty_Rate_ACS','NumAll_inPOV_ACS','PCTPOV017','POV017','Median_HH_Inc_ACS','POVALL'], axis = 1)


# In[79]:


final2


# In[39]:


print(final2['price'].corr(final2['PerCapitaInc']))


# In[40]:


print(final2.corr())


# In[41]:


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


# In[42]:


f,ax = plt.subplots(figsize=(15, 15))
sns.heatmap(final2.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()


# In[86]:


final2['price,percapitainc'] = final2['price'] / final2['PerCapitaInc']
final2


# In[96]:


max(final2['lat'])


# In[100]:


final2['lng'].value_counts()


# In[106]:


final2['status'] = final2['status'].replace(['for_sale'], 'sold')


# In[107]:


final2


# In[87]:


#final2.to_csv("final2.csv")


# In[115]:


import folium
from folium.plugins import HeatMap

map_hooray = folium.Map(location=[40.74173 ,-74.00037],
                    zoom_start = 2, min_zoom=2) 

heatmap = final2[final2['state_name']=='New York'] 
heatmap = heatmap[heatmap['status']=='sold'] 
heatmap = heatmap[['lat', 'lng']] 


    
    
folium.CircleMarker([40.74173 ,-74.00037],
                    radius=50,
                    popup='Homicide',
                    color='red',
                    ).add_to(map_hooray) 
    
heatmap_data = [[row['lat'],row['lng']] for index, row in heat_df.iterrows()]

HeatMap(heat_data, radius=10).add_to(map_hooray) 
map_hooray 


# In[ ]:




