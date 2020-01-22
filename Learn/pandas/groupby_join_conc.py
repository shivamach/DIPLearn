#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[5]:


p = {'item':['apple','apple','orange','orange','guns','guns'],'days':['mon','tue','wed','thur','fri','sat'],'sales':[100,80,200,100,5,10]}


# In[6]:


#is our dictionary
p


# In[8]:


df = pd.DataFrame(p)
df
#our panda dataframe for the same


# In[30]:


x = df.groupby('item')
print(x)
print(x.mean())
x.count()
#groupby puts all items of same type together and then we can put functions onit kinda i guess
#gourpby puts all the boys together


# In[35]:


print(x.max()) #gives max of item amount and which date
x = df.groupby('item')
#a table describing summary after groupin the dictionary by item name
x.describe().transpose


# In[28]:



x = pd.DataFrame(x)


#this is what a datframe generated from pandas.core.grouby.generic.DataFreameGroupBy object
#looks like


# In[36]:


#grouping stuff
x1 = {'a':[1,2,3,4],'b':[77,3,2,1]}
x2 = {'c':[2,5,7,9],'d':[13,69,42,0]}


# In[40]:


x = pd.DataFrame(x1,index=['p1','p2','p3','p4'])


# In[44]:


y = pd.DataFrame(x2,index=['p5','p1','p2','p8'])


# In[51]:


print(x.join(y)) #inner is by default
#other options outer,left,right
#inner joins only the common rows
#outer just brings all rows together and puts nan
#left puts lhs complete
#right puts rhs complete
print(x.join(y,how="right"))


# In[57]:


#concatenation
x1 = {'a':[1,1,1,1,1],'b':[1,1,1,1,1],'c':[1,1,1,1,1],'d':[1,1,1,1,1],'e':[1,1,1,1,1]}
x2 = {'e':[2,2,2,2,2],'f':[2,2,2,2,2],'g':[2,2,2,2,2],'h':[2,2,2,2,2],'i':[2,2,2,2,2]}
x3 = {'a':[3,3,3,3,3],'b':[3,3,3,3,3],'c':[3,3,3,3,3],'d':[3,3,3,3,3],'e':[3,3,3,3,3]}


# In[58]:


df1 = pd.DataFrame(x1,index=[1,2,3,4,5])
df2 = pd.DataFrame(x2,index=[1,2,3,4,5])
df3 = pd.DataFrame(x3,index=[5,6,7,8,9])
#making dataframes in specific style to show off concatenation


# In[62]:


pd.concat([df1,df2],axis=1)
#joins e columns if axis=0. axis 1 makes columns concatenate same ones


# In[63]:


pd.concat([df1,df2])
#as you can see


# In[64]:


pd.concat([df1,df3],axis=1)
#here 5 will be common. axis0 implies e will be taken common
#can concatenate multiple bishes too its cool


# In[70]:


#merging
df1 = pd.DataFrame({'key':[1,2,3],'a':[2,3,4],'b':[5,6,7]})
df2 = pd.DataFrame({'key':[1,2,3],'a':[2,5,9],'b':[5,6,7]})


# In[68]:


print(df1)
print(df2)


# In[75]:


#shift tab and read up lil about most commands imma be using
pd.merge(df1,df2,how="outer")
#to show that this has the outer option too
#merges the common columns by "how" groupby sorta


# In[83]:


pd.merge(df1,df2)
df2 = pd.DataFrame({'key':[1,2,3],'c':[2,5,9],'d':[5,6,7]})
#change c,d to b,c and so and see the difference that it causes in the next statement


# In[85]:


pd.merge(df1,df2,how="inner",on='key')
#we have key first in dict so normally it goes well, got to specify key for situations where
#multiple keys exist and or key is not first in the dict making the dateframe
#on=[key1,key2] is allowed , give multiple key


# In[ ]:




