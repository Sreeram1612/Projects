#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing py mongo
from pymongo import MongoClient


# In[2]:


#connecting server
client = MongoClient('mongodb://localhost:27017/')


# In[3]:


#database collection
client.list_database_names()


# In[4]:


#making connection with one database
db=client['foodsales']


# In[5]:


db.list_collection_names()


# In[6]:


for i in db.sales.find():
    print(i)


# In[7]:


#count no of orders in east region and west region.


# In[7]:


for i in db.sales.find({},{"Region":"East"}):
    print(i)


# In[8]:


#count no of orders in east region and west region.
w=db.sales.count_documents({"Region":"West"})
e=db.sales.count_documents({"Region":"East"})
print("Total count of orders in East region and West region are",w,"and",e)


# In[ ]:





# In[9]:


#Total number cities in data
a=db.sales.aggregate([{"$group":{"_id":"$City"}},{"$group":{"_id":"","count":{"$sum":1}}}]);
for i in a:
    print("total cities in foodsales data: ",i)


# In[24]:


#list of Region and City in data
a=db.sales.aggregate([{"$project":{"_id":0,"Region":1,"City":1}}])
for i in a:
    print(i)
    


# In[59]:


#two regions mentioned in data
print("Regions in data:")
a=list(db.sales.distinct("Region"))
for i in a:
    print(i)
    
print("Cities in data: ")
b=list(db.sales.distinct("City"))  
for j in b:
    print(j)


# In[22]:


c=db.sales.find({"Region":"East"})
for i in c:
    print( i["City"])


# In[30]:


#city wise sales
city=[{"$unwind":"$City"},{"$group":{"_id":"$City","sales":{"$sum":1}}}]
print(list(db.sales.aggregate(city)))


# In[61]:


q={"city":[("$near","East")]}
for i in db.sales.find(q):
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




