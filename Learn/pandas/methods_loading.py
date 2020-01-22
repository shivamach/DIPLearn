#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


x = pd.DataFrame({'a':[1,2,3,4,5],'b':[20,20,30,40,50]})


# In[3]:


x


# In[7]:


a = x.columns
print(a)


# In[5]:


x.index
#returns the info that is shown here right now


# In[8]:


x['b'].sum()
#add bitches in a column or so 


# In[9]:


def inc(x):
    x=x+100
    return x
#suppose wish to apply this whole function to a column , do next line


# In[10]:


x['b'].apply(inc)


# In[11]:


x.sort_values('b') #sort elements in a column
#indexes changes in whole table and other columns to according to ascending order of 
#column selected


# In[13]:


x['b'].unique()
#numpy array of unique values


# In[15]:


x['b'].nunique() #no of unique values


# In[16]:


x['b'].value_counts()
#each unique value and how many times it occurs


# In[17]:


x.isnull()
#is there a zero null anywhere in dataframe it will go true


# In[18]:


######loading data using pandas##############


# In[ ]:




