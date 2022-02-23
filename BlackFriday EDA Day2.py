#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#importing the train dataset
df_train=pd.read_csv("c:/test/BlackFriday/Train.csv")


# In[3]:


df_train


# In[4]:


# importing test dataset
df_test=pd.read_csv("c:/test/BlackFriday/Test.csv")


# In[5]:


df_test


# In[6]:


#merge both test and train datasets using append
df=df_train.append(df_test)  #appending and storing the new dataframe as df
df


# In[7]:


# checking the information about the dataset

df.info()


# ## observations: there are 3 float, 4 int and 5 object data type columns
# ## there are 783667 rows. NaN values are in Product_Category_2, Product_Category_3 and in Purchase columns.

# In[8]:


# checking the percentile, min, max

df.describe()


# In[9]:


# changing categorical feature into numerical ---- gender     changing male -----> 1  and female -----> 0

df['Gender']=df['Gender'].map({'F':0, 'M':1})
# map function changing female to 0 and male to 1


# In[10]:


df


# ## gender has changed to 0 and 1

# In[11]:


# handle categorical feature Age....  

# checking what are the different values in the Age coulmn
df['Age'].unique()


# ## as you can see there are different age groups. Lets assign values to age groups ...
# ## 0-17 ----> 1
# ## 18-25 ----> 2
# ## 26-35 ----> 3
# ## 36-45 ---> 4
# ## 46-50 ----> 5
# ## 51-55 ----->6
# ## 55+ ----->7

# In[12]:


df['Age']=df['Age'].map({'0-17':1, '18-25':2,'26-35':3, '36-45':4,'46-50':5, '51-55':6,'55+':7})


# In[13]:


df


# ## age is changed to numerics

# In[14]:


df['City_Category'].unique()


# ## we can see there are 3 different city categories

# ## lets change city categories by giving certain numbers....
# ##  A---->1
# ##  B---->2
# ##  C---->3

# In[15]:


df['City_Category']=df['City_Category'].map({'A':1, 'B':2, 'C':3})


# In[16]:


df


# ## city category has changed in to numbers

# In[17]:


df['Stay_In_Current_City_Years'].unique()


# ## you can observe, we need not change all the values in Stay_In_Current_City_Years, only 4+ should be changed
# ## lets change it to 4 (now 4 means 4+)

# In[18]:


df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].map({'0':0, '1':1, '2':2, '3':3, '4+':4})


# In[19]:


df


# ## Stay_In_Current_City_Years has also changed

# ## we dont need Product_ID and User_ID
# ## lets remove the columns

# In[20]:


df.drop(columns = ['User_ID', 'Product_ID'], inplace=True)


# In[21]:


df


# ## User id and product id columns are dropped

# ## _________________________________

# In[22]:


df.info()


# ## now if you check the data types of columns, they are all numeric

# ## -----------------------------------------------------------------------------------------------------------

# ## Drawing plots and analysing data

# In[23]:


df.columns


# In[24]:


## checking Genderwise purchase

sns.barplot(x='Gender', y='Purchase', data=df)
plt.xlabel("Female=0, Male=1")
plt.show()


# ## observation:  Male are purchasing slightly more than Female

# In[25]:


## dealing with null values
df['Product_Category_1'].mode()


# In[26]:


df['Product_Category_2'].mode()


# In[27]:


df['Product_Category_3'].mode()


# ## observation: mode of product category 1 is 5
# ## that of product category 2 is 8.0
# ## that of product category 3 is 16.0

# ## lets replace NaN values with the respective modes

# In[28]:


df['Product_Category_1'].fillna(5,inplace=True)


# In[29]:


df['Product_Category_2'].fillna(8.0,inplace=True)


# In[30]:


df['Product_Category_3'].fillna(16.0,inplace=True)


# In[31]:


df.info()


# ## you can see there are no null values in product categories

# In[32]:


df.isnull().sum()  #checning how many null values are there in Purchase


# In[33]:


df.columns


# In[34]:


df[df['Purchase'].isna()]  # displaying all the rows with NaN values


# In[35]:


df[df['Purchase'].isna()].groupby("Product_Category_1").size()


# In[36]:


df[df['Purchase'].isna()].groupby("Product_Category_2").size()


# In[37]:


df[df['Purchase'].isna()].groupby("Product_Category_3").size()


# ## lets change product_category_3 NaN Purchase column values with average of product_category_3 purchase values
# ## because there are 176395 records with NaN values

# In[38]:


# getting rows which have purchase_category_3=16.0 and Purchase = NaN
condition1 = (df['Product_Category_3'] == 16)
condition2 = (df['Purchase'].isnull())
condition3 = condition1 & condition2


# In[39]:


df[condition3]


# In[40]:


# getting rows which have purchase_category_3=16.0 and Purchase = NOT NULL
condition4 = (df['Product_Category_3'] == 16)
condition5 = (~df['Purchase'].isnull())
condition6 = condition4 & condition5


# In[41]:


df[condition6]


# In[42]:


# finding the average of the non null values with product category 3.
df[condition6].mean()


# ## we can see the mean is 8516.9
# ## lets replace product_category_3 NaN values with 8517

# In[43]:


df['Purchase'].fillna(8517, inplace=True)


# In[44]:


df


# In[45]:


df.isnull().sum()


# ## there are no null values in the dataframe

# ## ----------------------------------------------------------------------------------------------------

# ## plotting graphs and analysing data

# In[46]:


sns.barplot(x='Age', y='Purchase', data=df)


# ## observation: Almost all the age groups are purchasing equally

# In[47]:


sns.barplot(x='Marital_Status', y='Purchase', data=df)


# ## observation: Married and Unmarried are purchasing equally

# In[48]:


sns.barplot(x='Stay_In_Current_City_Years', y='Purchase', data=df)


# ## observation: people who are staying in the city for 1,2,3,4, or more years are purchasing equally

# In[49]:


sns.barplot(x='Gender', y='Purchase', data=df)


# ## Female:0 and Male:1
# ## Observation: Men are purchasing slightly more than Women

# In[50]:


sns.countplot(x='Gender',data=df)


# ## observation: number of men who are purchasing is a lot more than women. But when you check the previous graph the amount for men and women was almost equal. Which means men are purchasing low cost items whereas women are purchasing costly items

# In[51]:


sns.countplot(x='Marital_Status',data=df)


# ## observation: Unmarried are purchasing more than married. 
# ## but the purchase amount was almost equal. Which means married are purchasing costly items

# In[52]:


sns.relplot(x="Gender", y="Purchase", data=df)


# In[53]:


sns.boxplot(x="Gender", y="Purchase", data=df)


# In[54]:


plt.scatter(x="Gender",y="Purchase", data=df)


# In[55]:


plt.scatter(x="City_Category",y="Purchase", data=df)


# In[56]:


sns.boxplot(x="City_Category", y="Purchase",data=df)


# In[ ]:




