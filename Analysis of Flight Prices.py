#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# load the dataset
df=pd.read_excel("Data_Train.xlsx")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.sample(15)


# In[ ]:





# In[ ]:





# In[6]:


# ANALYSIS ON TRAIN DATASET
print("EDA ON DATASET")
print("#"*30)
print(df.info())


# In[7]:


# Statistical view
print("EDA ON DATASET")
print("#"*30)
print(df.describe())


# In[8]:


# convert Date_of_journey to date
df['Date'] = pd.to_datetime(df.Date_of_Journey, format='%d/%m/%Y')
df.head()


# In[9]:


df['month'] = pd.to_datetime(df.Date_of_Journey, format='%d/%m/%Y').dt.month
df.head()


# In[10]:


df.drop(['Date_of_Journey'],axis=1,inplace=True)
df.drop(['Journey_Month'],axis=1,inplace=True)


# In[20]:


df


# In[17]:


df['day'] = pd.to_datetime(df.Date, format='%d/%m/%Y').dt.day
df.head()


# In[71]:


## Convert the Duration to numeric 
l=list(df['Duration'])
h=0
m=0
d=[]
for i in l:
    s=str(i).split(" ")
    if len(s)==2:
        if 'h' in s[0]:
            h=s[0].split('h')
        if 'm' in s[1]:
            m=s[1].split('m')
    if len(s)==1:
        if 'h' in s[0]:
            h=s[0].split('h')
        if 'm' in s[0]:
            m=s[0].split('m')
    d.append((int(h[0])*60+int(m[0])))
    h=[0]
    m=[0]
d


# In[72]:


df.drop(['minutes'],axis=1,inplace=True)


# In[74]:


df['minutes']=d
df[['Duration','minutes']].sample(20)


# In[81]:


df['dep_time'] = pd.to_datetime(df.Dep_Time, format='%H:%M').dt.time
df.head(60)


# In[82]:


df.info()


# In[83]:


df


# In[13]:


# get source destination for every airline with maximum price
airlines=df.groupby('Airline')
df_mp=pd.DataFrame(airlines["Price"].max())
df_mp
df1=df[["Airline","Source","Destination","Route","Price"]]
df2=pd.merge(df_mp,df1,left_on=["Airline","Price"],right_on=["Airline","Price"])
df2.drop_duplicates()


# In[14]:


airlines=df.groupby('Airline')
df_mp=pd.DataFrame(airlines["minutes"].max())
df_mp
df1=df[["Airline","Source","Destination","Route","minutes"]]
df2=pd.merge(df_mp,df1,left_on=["Airline","minutes"],right_on=["Airline","minutes"])
df2.drop_duplicates().reset_index()


# In[15]:


df.value_counts("Source")


# In[16]:


df.value_counts("Destination")


# In[17]:


s=input("Enter the source")
d=input("Enter the destination")
m=int(input("Enter the Month of travel"))
f=np.where((df["Source"]==s) & (df["Destination"]==d) &(df["month"]==m))
df1=df.loc[f]
df1
df1[["Airline","Source","Destination","Route","Duration","Total_Stops","Price","Additional_Info"]].drop_duplicates().sample(15)


# In[126]:


df


# In[138]:


sns.pairplot(df)


# In[18]:


df1=df[["Airline","month","Price"]]
df2=df1.groupby(["Airline","month"])
df3=pd.DataFrame(df2["Airline","Price"].mean()).reset_index().round()
df4=df3.pivot("Airline","month","Price")
df4
sns.heatmap(df4,cmap="BuGn",annot=True, fmt='.1f')


# In[188]:


df.value_counts("Total_Stops")


# In[191]:


sns.relplot(data=df,x="minutes",y="Price",hue="Total_Stops")


# In[ ]:




