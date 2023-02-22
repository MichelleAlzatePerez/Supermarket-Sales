#!/usr/bin/env python
# coding: utf-8

# # Import External Libaries
# pandas libary for data manipulation
# numpy for scientific computing
# matplotlib and seaborn for data visualization
# calmap for calendar and heat map
# panda_profiling to streamline EDA

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Read in dataset and view first five rows

# In[7]:


df = pd.read_csv('supermarket_sales.csv')


# In[8]:


df.head()


# In[9]:


df.columns


# In[10]:


df.dtypes


# In[12]:


df['Date'] = pd.to_datetime(df['Date'])


# In[14]:


df.dtypes


# In[15]:


df.set_index('Date', inplace=True)


# In[16]:


df.head()


# # Calculating Quick Summary Statistics

# In[17]:


df.describe()


# # Distribution Plot of Customer Ratings

# In[41]:


sns.distplot(df['Rating'])

plt.axvline(x=np.mean(df['Rating']),label='mean')

plt.axvline(x=np.percentile(df['Rating'],25),c='green',label='25th-75th percentile')

plt.axvline(x=np.percentile(df['Rating'],75),c='green')

plt.legend()


# In[44]:


df.hist(figsize=(10,10))


# # Do aggregate sales numbers differ much between branches?

# In[45]:


sns.countplot(df['Branch'])


# In[47]:


df['Branch'].value_counts()


# In[48]:


sns.countplot(df['Payment'])


# # Are ratings influenced by gross income

# In[50]:


sns.regplot(df['Rating'], df['gross income'])


# # no relation between ratings and gross income

# In[51]:


sns.boxplot(x=df['Branch'],y=df['gross income'])


# # No variation in gross incomes between the different branches

# In[52]:


sns.boxplot(x=df['Gender'],y=df['gross income'])


# # Is there a noticeable time trend in gross income?

# In[53]:


df.groupby(df.index).mean()


# In[54]:


sns.lineplot(x=df.groupby(df.index).mean().index,
            y=df.groupby(df.index).mean()['gross income'])


# # Duplicate Rows and Missing Values

# In[59]:


df.duplicated()


# In[60]:


df.duplicated().sum()


# In[61]:


df.isna().sum()


# # Correlation Analysis

# In[63]:


np.corrcoef(df['gross income'], df['Rating'])


# In[65]:


round(np.corrcoef(df['gross income'], df['Rating'])[1][0],2)


# In[66]:


df.corr()


# In[67]:


np.round(df.corr(),2)


# In[69]:


sns.heatmap(np.round(df.corr(),2),annot=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




