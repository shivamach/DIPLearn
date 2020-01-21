#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#importing the required libraries


# In[8]:


x = ['a','b','c','d','e','f','g','h',] #list alpha
y = [1,2,3,4,5,6,7,8] #list num
z = {"one":'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}#matching dict


# In[3]:


a = pd.Series(data = x)
#pd.Series(x) if only using on paramters, need data= if 1+ parameters


# In[5]:


print(a)
#a is a series with no boundary. a has its values enumerated and put into a table
type(a)


# In[10]:


a = pd.Series(data=x,index=y) #if in same order specifying names can avoid
#pd.Series(data,indix,dtype,name,copy,fastPath)
A = pd.Series(y,x)
print(a)
print(A)
aa = pd.Series(z)
#a dictionary need not use index wala cheez in series
#a dictionary automatically will assign key as indexes and values as values


# In[11]:


print(aa)


# In[14]:


#user can add two lists. values assigned to same indexed are added and others are kept as it is
#if no common indexes found then all indexes kept with nan values
print(a+A)


# In[15]:


print(a+aa)
#one can see that all common index values were added while non common indexes had their
#value replaced with Nan


# In[18]:


#to access a series_name(key)
print(A['c'])
A['c':]
#indexing slicing works like dictionaries
#press shifttab after entering a command here to see help


# In[21]:


A = [1,2,3,4]
B = [2,54,6,7]
C = [5,32,1,8]
D = [6,9,4,2]
E = [4,2,0,9]


# In[38]:


df = pd.DataFrame([A,B,C,D,E],['a','b','c','d','e'],['one','two','three','four'])
#pd.DataFrame(data,indexes,columns)
#data is a list of lists, indexes is a list with len = no of lists in data
#makes a table with column headinga entered as list. no of columns = no of max length of list in data lists of li
print(df)
#figure out what happens if you pass a dictionary in this instead


# In[53]:


#you can add and remove rows and columns in dataframe
df['five'] = df['four'] + df['one']
print(df)

#creating a new row and column using other rows or columns respectively


# In[54]:


df.drop('e')


# In[59]:


print(df)
#drop doest remove permanently, but it returns a boi with deleted. to do in place do inplace=True
df.drop('e', inplace=True)


# In[60]:


df.drop('five',axis=1,inplace=True)
#rows are indexes and default, axis 0
#columns gotta specify axis 1
print(df)
#remove the inplace parameter to return another dataframe with the mentioned dropk 


# In[72]:


rowa = (df.loc['a'])
print(rowa)
type(rowa)


# In[74]:


rowa == df.iloc[0]
#to access rows using integers rather then rowlabels use iloc
#indexes exit only for rows none for columns


# In[80]:


#to access elements do
a = df.loc['a','two']
b = df.iloc[0,1]
a == b


# In[ ]:





# In[ ]:




