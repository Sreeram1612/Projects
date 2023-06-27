#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import mpl_toolkits
from plotly.offline import iplot
import plotly as py
import plotly.tools as tls
import cufflinks as cf


# In[4]:


df=pd.read_csv("training.csv")
df


# In[11]:


df.info()


# In[10]:


df.describe()


# In[12]:


df.head()


# In[13]:


df.tail()


# In[14]:


df.sample(5)


# In[15]:


df.shape


# In[16]:


df.isnull().sum()


# In[17]:


df.fillna(0,inplace=True)
df


# In[18]:


df.isnull().sum()


# In[19]:


df.info()


# In[20]:


df.columns


# In[21]:


df.drop(['index'],axis=1,inplace=True)
df.head()


# In[124]:


df[df["age"]==0]
df[df["age"]>99]


# In[26]:


df.drop(df[df['age']==0].index,inplace=True )
df.drop(df[df['age']>99].index,inplace=True)


# In[27]:


df[df["age"]==0]
df[df["age"]>99]


# In[28]:


sns.lineplot(df["NumberOfDependents"],df['SeriousDlqin2yrs'])


# In[38]:


sns.boxplot(df['SeriousDlqin2yrs'],df["NumberOfOpenCreditLinesAndLoans"])


# In[44]:


sns.lineplot(y=df["SeriousDlqin2yrs"],x=df["NumberRealEstateLoansOrLines"])


# In[46]:


sns.barplot(df['SeriousDlqin2yrs'],df['age'])


# In[47]:


sns.heatmap(df.corr())


# In[56]:


plt.hist(x="NumberOfOpenCreditLinesAndLoans")


# In[69]:


sns.barplot(df['NumberOfTime30-59DaysPastDueNotWorse'],df["NumberOfTime60-89DaysPastDueNotWorse"])


# In[70]:


sns.boxplot(df['SeriousDlqin2yrs'],df["age"])


# In[71]:


sns.boxplot(df['NumberRealEstateLoansOrLines'],df["NumberOfOpenCreditLinesAndLoans"])


# In[72]:


sns.boxplot(df['NumberRealEstateLoansOrLines'],df["NumberOfDependents"])


# In[74]:


sns.lineplot(df['NumberRealEstateLoansOrLines'],df["NumberOfOpenCreditLinesAndLoans"])


# In[79]:


sns.lineplot(df['NumberRealEstateLoansOrLines'],df["NumberOfDependents"])


# In[80]:


sns.lineplot(df['NumberOfTime30-59DaysPastDueNotWorse'],df["NumberOfTime60-89DaysPastDueNotWorse"])


# In[ ]:





# In[ ]:




