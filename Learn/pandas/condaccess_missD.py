#!/usr/bin/env python
# coding: utf-8

# In[1]:


#type command in jupyter notebook and type in shift+tab to see what that argument needs
A = [1,2,3,4]
B = [9,6,2,5]
C = [2,8,0,9]
D = [1,0,2,4]


# In[3]:


import numpy as np
import pandas as pd


# In[9]:


df = pd.DataFrame([A,B,C,D],['A','B','C','D'],['ONE','TWO','THREE','FOUR'])


# In[5]:


print(df)
#created the base dataframe going to work on for these parts


# In[6]:


df > 2
#this will return table with same xy indexes but bool values


# In[7]:


df[df>2]
#this will keep the value at true places while nan all others


# In[12]:


df[df['ONE']>1]
#this will print complete rows for the rows where column'one' satisfies our condition


# In[13]:


df[df['ONE']>1][['ONE','FOUR']]
#note the double bracket
#suppose in above output you only care about first and last column results for condition on first col


# In[14]:


#for multiple conditions use conditional operatores our bff & | ~ all that 
#now missing data now


# In[18]:


d = {'a':[1,2,3,4,5],'b':[6,7,8,9,np.nan],'c':[10,11,12,np.nan,np.nan],'d':[3,4,np.nan,np.nan,np.nan],'e':[69,np.nan,np.nan,np.nan,np.nan]} 
#the missing value
d


# In[20]:


df = pd.DataFrame(d)
df
#now DataFrame had (datalist,rowlist,axislist)
#when a dictionary is passed with each key having a list, each key becomes axislist with
#autonumeric rowlist indexes assigned with values inside
#also it can be seen that here when np is used the dtype becomes float
#while without np the column as dtype int64


# In[32]:


#practice dictionary
e = {'one':[1,2,3,4]}
df2 = pd.DataFrame(e,['a','b','c','d'],['one']) # == pd.Dataframe(e) here
print(df2)
#observes that any name for row can be changed and max(size of list) no of indexes given
#also that axisindex can be given but same as key list of dictionary
#if diff name passed nan comes
df3 = pd.DataFrame(e,['a','b','c','d'],['ONE'])
print()
print(df3)
del(df2)
del(df3)


# In[36]:


df.dropna()#all rows with nan dropped
df.dropna(axis=1) #axis=0 is default


# In[37]:


df.dropna(thresh=3)
#drops all rows where more than or equal to three nans there


# In[38]:


df.dropna(axis=1,thresh=3)# same thing as above line but with columns


# In[41]:


#sometimes we need nan to be replaced with a dummy value to get shit done and such a dummy so
#it wont affect other values, we gotta use brains
df.fillna(1)
#to fill nan with 1
df['b'].fillna(value=df['b'].mean())
#this second line is a wowww
#it fills na in column b with value which is mean of all values of column b


# In[42]:


df.iloc[2].fillna(value=df.iloc[2].mean())
#same above thing to do for a row , which is stored as a series in the end


# In[ ]:




