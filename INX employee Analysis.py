#!/usr/bin/env python
# coding: utf-8

# # INX Future Employee Performance Analysis

# Importing Libraries

# In[1]:


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
from matplotlib import pyplot as plt
from sklearn.preprocessing  import StandardScaler


# In[2]:


df=pd.read_csv("INX.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.sample(20)


# In[6]:


#shape of the dataset
df.shape


# In[7]:


# info of the datatype
df.info()


# In[10]:


# corr() is used to find co-relation between the columns
df.corr()


# In[11]:



df.describe()


# In[12]:


#To get the null values
df.isnull().sum()


# In[13]:


df['EmpDepartment'].unique()


# In[18]:


df['EducationBackground'].unique()


# In[19]:


df['Age'].unique()


# In[20]:


df["EmpRelationshipSatisfaction"].unique()


# In[21]:


df['PerformanceRating'].unique()


# In[22]:


df['MaritalStatus'].unique()


# In[23]:


df['EmpWorkLifeBalance'].unique()


# In[25]:


sns.countplot(df["EducationBackground"])
plt.xticks(rotation=45,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('EducationBackground',fontsize=10)
plt.ylabel('PerformanceRating',fontsize=10)
plt.title("Performance Rating based of Educational background",fontsize=10,fontweight="bold")
plt.show()


# In[28]:


sns.heatmap(df.corr())


# In[32]:


sns.countplot(df["Gender"])
plt.xticks(rotation=45,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Gender',fontsize=10)
plt.ylabel('EducationBackground',fontsize=10)
plt.title("Gender based of Educational background",fontsize=10,fontweight="bold")
plt.show()


# In[43]:


sns.set_theme(style="whitegrid")
plt.xticks(rotation=45,fontsize=10)
plt.yticks(fontsize=10)
sns.barplot(df["EducationBackground"],df['PerformanceRating'])


# In[47]:


ax=plt.axes()
ax.set(facecolor="grey")
sns.countplot(x="EducationBackground",hue="Gender",data=df,palette="magma",saturation=1)
plt.xticks(rotation=45,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("\n EducationBackground",fontsize=15)
plt.ylabel("Gender",fontsize=15)
plt.title("Total counts in male and female",fontsize=12,fontweight="bold")
plt.show()


# In[54]:


df.boxplot('Age');


# In[68]:


plt.figure(figsize=(16,9))

sns.lineplot(x='EmpDepartment', y='PerformanceRating', data=df, hue="EmpWorkLifeBalance",style="EmpRelationshipSatisfaction",palette='hot',
             dashes=False,markers=['X','v',"o","<"],legend='brief')
plt.xlabel("EmpDepartment")


# In[75]:


ax=plt.axes()
ax.set(facecolor="pink")
sns.countplot(x="EmpDepartment",hue="Gender",data=df,palette="magma",saturation=1)
plt.xticks(rotation=45,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("\n EmpDepartment",fontsize=15)
plt.ylabel("Gender",fontsize=15)
plt.title("Total counts in male and female",fontsize=12,fontweight="bold")
plt.show()


# In[81]:


ax=plt.axes()
ax.set(facecolor="black")
sns.countplot(x="EmpDepartment",hue="MaritalStatus",data=df,palette="magma",saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("\n EmpDepartment",fontsize=15)
plt.ylabel("MaritalStatus",fontsize=15)
plt.title("Total employees in male and female",fontsize=12,fontweight="bold")
plt.show()


# In[87]:


sns.set_theme(style="darkgrid")
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
sns.barplot(df["Gender"],df['PerformanceRating'])


# In[89]:


sns.set_theme(style="darkgrid")
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
sns.lineplot(df["MaritalStatus"],df['PerformanceRating'],marker='o')


# In[92]:


sns.set_theme(style="whitegrid")
plt.xticks(rotation=45,fontsize=10)
plt.yticks(fontsize=10)
sns.lineplot(df["EducationBackground"],df['TotalWorkExperienceInYears'],marker='^',linestyle=":")


# In[95]:


sns.barplot(df["EmpRelationshipSatisfaction"],df['EmpWorkLifeBalance'])


# In[98]:


sns.lineplot(df["MaritalStatus"],df["EmpWorkLifeBalance"],marker="o",color="k")


# In[100]:


sns.set_theme(style="darkgrid")
plt.xticks(rotation=45,fontsize=10)
plt.yticks(fontsize=10)
sns.lineplot(df["EducationBackground"],df['EmpEducationLevel'],marker='^',color="#6A5ACD",linestyle=":")


# In[104]:


sns.lineplot(df["MaritalStatus"],df["EmpRelationshipSatisfaction"],marker="o",color='r')


# In[107]:


sns.barplot(df["ExperienceYearsInCurrentRole"],df["ExperienceYearsAtThisCompany"],color="#F08080")


# In[109]:


sns.barplot(df["DistanceFromHome"],df["ExperienceYearsAtThisCompany"],color="rosybrown")


# In[112]:


dept = df.iloc[:,[5,27]].copy()
dept_per = dept.copy()
print(dept_per)


# In[113]:


dept_per.groupby(by='EmpDepartment')['PerformanceRating'].mean()


# In[116]:


dept_per.groupby(by='EmpDepartment')['PerformanceRating'].value_counts()


# In[120]:


department = pd.get_dummies(dept_per['EmpDepartment'])
performance = pd.DataFrame(dept_per['PerformanceRating'])
dept_rating = pd.concat([department,performance],axis=1)


# In[122]:


background_Edu = df.iloc[:,[3,27]].copy()
background_Edu_per = background_Edu.copy()


# In[123]:


background_Edu_per.groupby(by='EducationBackground')['PerformanceRating'].mean()


# In[124]:


background_Edu_per.groupby(by='EducationBackground')['PerformanceRating'].value_counts()


# In[125]:


department1 = pd.get_dummies(background_Edu_per['EducationBackground'])
performance1 = pd.DataFrame(background_Edu_per['PerformanceRating'])
dept_rating = pd.concat([department1,performance1],axis=1)


# In[157]:


plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Marketing'])
plt.subplot(2,3,2)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Life Sciences'])
plt.subplot(2,3,3)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Human Resources'])
plt.subplot(2,3,4)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Medical'])
plt.subplot(2,3,5)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Other'])
plt.subplot(2,3,6)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Technical Degree'])
plt.show()


# In[135]:


Emp_dept1 = df.iloc[:,[5,10]].copy()
Emp_dept1_per = Emp_dept1.copy()


# In[136]:


Emp_dept1_per.groupby(by='EmpDepartment')['EmpEnvironmentSatisfaction'].mean()


# In[137]:


Emp_dept1_per.groupby(by='EmpDepartment')['EmpEnvironmentSatisfaction'].value_counts()


# In[139]:


department2 = pd.get_dummies(Emp_dept1_per['EmpDepartment'])
performance2 = pd.DataFrame(Emp_dept1_per['EmpEnvironmentSatisfaction'])
dept_rating = pd.concat([department2,performance2],axis=1)


# In[154]:


plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
sns.barplot(dept_rating['EmpEnvironmentSatisfaction'],dept_rating['Sales'])
plt.subplot(2,3,2)
sns.barplot(dept_rating['EmpEnvironmentSatisfaction'],dept_rating['Development'])
plt.subplot(2,3,3)
sns.barplot(dept_rating['EmpEnvironmentSatisfaction'],dept_rating['Research & Development'])
plt.subplot(2,3,4)
sns.barplot(dept_rating['EmpEnvironmentSatisfaction'],dept_rating['Human Resources'])
plt.subplot(2,3,5)
sns.barplot(dept_rating['EmpEnvironmentSatisfaction'],dept_rating['Finance'])
plt.subplot(2,3,6)
sns.barplot(dept_rating['EmpEnvironmentSatisfaction'],dept_rating['Data Science'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




