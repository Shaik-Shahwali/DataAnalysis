#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis on Zomato dataset Day1

# In[1]:


#importing all the libraries needed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("c:/test/zomato/zomato.csv", encoding='latin-1' )  #if encoding isnot given it shows error


# In[3]:


df


# In[4]:


df.columns  #checking the columns


# In[5]:


df.info()


# ## there are null values in cuisines column

# In[6]:


df.describe()  #displays only numerical columns


# ## in data analysis what things we do
# 1) missing values
# 
# 2) explore abput numerical variables
# 
# 3) explore about categories variables
# 
# 4) finding relationship between features/columns
# 

# In[7]:


df.isnull().sum() #checking null values


# ## in cuisines there are 9 missing values

# In[8]:


[features for features in df.columns if df[features].isnull().sum()>0]  #displays the column name which has null values


# ## using heatmap to find the null values

# In[9]:


plt.figure(figsize=(12,10)) # if the size of the graph is not increased, cant see the nan values on graph
sns.heatmap(df.isnull(),yticklabels=False, cbar=False,cmap='viridis') ## this will show the null values in graph


# ## not able to see, as there are only 9 NaN values and there are over 9500 records.

# In[10]:


# reading country code file

df_country = pd.read_excel("c:/test/zomato/Country-Code.xlsx")
df_country


# ## zomato has business in 15 countries

# In[11]:


## merging two dataframes based on country code. because contry code is in both the data frames
final_df = pd.merge(df,df_country, on="Country Code", how="left")
final_df


# ## first we had 21 columns now we have 22

# In[12]:


# data types can also be checked like this

final_df.dtypes


# ## exploring the dataset

# In[13]:


final_df.columns


# In[14]:


final_df.groupby('Country').size()


# ## we can conclude that zomato has most of its business in India

# In[15]:


final_df.Country.value_counts() # gives the same result as above.

#store it in country names variable

country_names = final_df.Country.value_counts().index


# In[16]:


country_names


# In[17]:


country_values = final_df.Country.value_counts().values


# In[18]:


country_values


# In[19]:


# pie chart

plt.pie(country_values, labels=country_names)


# In[20]:


# pie chart 
# top three countries

plt.pie(country_values[:3], labels=country_names[:3])


# In[21]:


#adding percentage in pie chart

plt.pie(country_values[:3], labels=country_names[:3], autopct='%1.2f%%')


# ## Observation: Most of the business of zomato is in India

# In[22]:


final_df.columns


# In[23]:


# check from which country more rating is coming

final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text' ]).size()


# In[24]:


# changing the column name to rating count
final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text' ]).size().reset_index().rename(columns={0:'Rating Count'})


# In[25]:



ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text' ]).size().reset_index().rename(columns={0:'Rating Count'})


# In[26]:


ratings


# ## observations: 
# 1) when rating is between 4.5 to 4.9  -----> excellent
# 2) when rating is between 4.0 to 4.4  -----> very good
# 3) when rating is between 3.5 to 3.9 -----> good
# 4) when rating is between 3.0 to 3.4 -----> avarage 
# and so on 

# In[27]:


ratings.head()


# In[28]:


# barplot 
# checking aggregate rating and rating count
plt.figure(figsize=(10,8))
sns.barplot(x="Aggregate rating", y="Rating Count", data=ratings)
plt.show()


# ## observation: above 2000 people did not rate at all

# In[29]:


## find the countries that have given 0 rating.

# final_df[['Aggregate rating','Rating color','Country']]
# based on rating color or aggregate rating we can get the countries which have given 0 rating

final_df[final_df["Rating color"]=="White"].groupby("Country").size()


# ## observation:
# 1) Brazil gave 5 zero ratings
# 2) India gave 2139 zero ratings
# 3) UK gave 1 zero rating
# 4) US gave 3 zero rating

# In[30]:


# how should we find the above result using Aggregate rating????


# In[31]:


#finding which country uses which currency

final_df[["Currency","Country"]].groupby(['Currency','Country']).size().reset_index()


# In[32]:


#which countries have online delivery option
final_df.columns


# In[33]:


final_df.head()


# In[34]:


final_df[final_df["Has Online delivery"]=="Yes"].groupby("Country").size()


# In[35]:


final_df[final_df["Has Online delivery"]=="Yes"].groupby("Country").size().reset_index()


# ## observation: India and UAE are the only countries that have online delivery option

# In[ ]:




