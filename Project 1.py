#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv('data.csv')


# In[4]:


data


# In[5]:


data.head(60)


# In[6]:


data.tail(60)


# In[7]:


data.info()


# In[8]:


data['fixed acidity'].info()


# In[9]:


data.dropna(inplace= True)


# In[10]:


data


# In[11]:


data.duplicated()


# In[12]:


data.info()


# In[13]:


data.describe()


# In[14]:


data.ID.describe()


# In[15]:


data['fixed acidity'].describe()


# In[16]:


data['volatile acidity'].describe()


# In[17]:


data['citric acid'].describe()


# In[18]:


data['residual sugar'].describe()


# In[19]:


data.chlorides.describe()


# In[20]:


data['free sulfur dioxide'].describe()


# In[21]:


data['total sulfur dioxide'].describe


# In[22]:


data.density.describe()


# In[23]:


data.pH.describe()


# In[24]:


data.sulphates.describe()


# In[25]:


data.alcohol.describe()


# In[26]:


data.alcohol.mode()


# In[27]:


data.quality.describe()


# In[28]:


x = data['fixed acidity'] < data['fixed acidity'].mean()
x.value_counts()


# In[29]:


lb= ['below mean','above mean']
plt.title('pie plot of fixed acidity')
plt.pie(x.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# ###  PIE PLOT AND HISTOPGRAM

# In[33]:


e=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
plt.hist(data['fixed acidity'],e,ec='black')
plt.xlabel('fixed acidity value')
plt.ylabel('ID')


# In[36]:


plt.hist(data)


# In[37]:


data['fixed acidity']


# 

# In[40]:


z = data['volatile acidity'] < data['volatile acidity'].mean()
z.value_counts()

lb= ['below mean','above mean']
plt.title('pie plot of volatile acidity')
plt.pie(z.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[41]:


plt.hist(data['volatile acidity'])
plt.xlabel('volatile value')
plt.ylabel('ID')


# In[42]:


t = data['citric acid'] < data['citric acid'].mean()
t.value_counts()
lb= ['below mean','above mean']
plt.title('pie plot of citric acid')
plt.pie(t.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[43]:


plt.hist(data['citric acid'])
plt.xlabel('citric value')
plt.ylabel('ID')


# In[47]:


w = data['residual sugar'] < data['residual sugar'].mean()
lb= ['below mean','above mean']
plt.title('pie plot of residual sugar')
plt.pie(w.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[45]:


plt.hist(data['residual sugar'])
plt.xlabel('residual value')
plt.ylabel('ID')


# In[63]:


b = data['chlorides'] < data['chlorides'].mean()
x.value_counts()

lb= ['below mean','above mean']
plt.title('pie plot of chlorides')
plt.pie(b.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[68]:


plt.hist(data['chlorides'])
plt.xlabel('chlorides value')
plt.ylabel('ID')


# In[48]:


a= data['free sulfur dioxide'] < data['free sulfur dioxide'].mean()
a.value_counts()
lb= ['below mean','above mean']
plt.title('pie plot of free sulfur dioxide')
plt.pie(a.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[49]:


plt.hist(data['free sulfur dioxide'])
plt.xlabel('free sulfur dioxide')
plt.ylabel('ID')


# In[62]:


l= data['total sulfur dioxide'] < data['total sulfur dioxide'].mean()
lb= ['below mean','above mean']
plt.title('pie plot of total sulfur dioxide')
plt.pie(l.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[72]:


plt.hist(data['total sulfur dioxide'])
plt.xlabel('total sulfur value')
plt.ylabel('ID')


# In[61]:


n= data['density'] < data['density'].mean()
lb= ['below mean','above mean']
plt.title('pie plot of density')
plt.pie(n.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[55]:


plt.hist(data['density'])
plt.xlabel('density value')
plt.ylabel('ID')


# In[60]:


g= data['pH'] < data['pH'].mean()
lb= ['below mean','above mean']
plt.title('pH')
plt.pie(g.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[76]:


plt.hist(data['pH'])
plt.xlabel('PH value')
plt.ylabel('ID')


# In[59]:


o= data['sulphates'] < data['sulphates'].mean()
lb= ['below mean','above mean']
plt.title('sulphates')
plt.pie(o.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[78]:


plt.hist(data['sulphates'])
plt.xlabel('sulphates value')
plt.ylabel('ID')


# In[64]:


c= data['alcohol'] < data['alcohol'].mean()
lb= ['below mean','above mean']
plt.title('pie plot of alcohol')
plt.pie(c.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[80]:


plt.hist(data['alcohol'])
plt.xlabel('alcohol value')
plt.ylabel('ID')


# In[65]:


q= data['quality'] < data['quality'].mean()
lb= ['below mean','above mean']
plt.title('pie plot of quality')
plt.pie(q.value_counts(),labels = lb, autopct = '%.2f%%', radius = 1 )


# In[82]:


plt.hist(data['quality'])
plt.xlabel('quality value')
plt.ylabel('ID')


# In[38]:


data_correlation = data.corr()
data_correlation


# In[ ]:





# In[39]:


plt.figure(figsize = (10,10))
sb.heatmap(data_correlation, annot= True, cmap= 'hot')

