#!/usr/bin/env python
# coding: utf-8

# In[7]:


from pymongo import MongoClient


# In[8]:


client= MongoClient('mongodb://localhost:27017/')


# In[10]:


#listing data bases
client.list_database_names()


# In[12]:


#taking connection with one db
db=client ["ODI_results"]


# In[13]:


#getting the name of collection inside the database
db.list_collection_names()


# In[14]:


#documents
for i in db.result.find():
    print(i)


# In[17]:


#count of documents
db.result.count_documents({})


# In[19]:


for i in db.result.find({},{'_id':0}):
    print(i)


# In[22]:


db.result.distinct('Country')


# In[24]:


db.result.distinct('Ground')


# In[25]:


db.result.distinct('Match_ID')


# In[27]:


#country and result wise count
a=db.result.aggregate([{"$group":{'_id':{'country':"$Country",'result':"$Result"},'count':{"$count":{}}}}])
for i in a:
    print(i)


# In[29]:


#list of win matches
a=db.result.aggregate([{'$match':{'Result':"won"}}])
for i in a:
    print(i)


# In[30]:


#batting first and win matches
a=db.result.aggregate([{'$match':{'Result':"won",'Bat':'1st'}}])
for i in a:
    print(i)


# In[31]:


#batting second and win matches
a=db.result.aggregate([{'$match':{'Result':"won",'Bat':'2nd'}}])
for i in a:
    print(i)


# In[46]:


for i in db.result.find({},{'_id':0,'Country':1,"Result":1}):
    print(i)


# In[63]:


a=db.result.aggregate([{"$group":{'_id':{'country':"$Country",'oppositon':'$Opposition','result':"$Result"}}}])
for i in a:
    print(i)


# In[32]:


db.batsman_data.count_documents({})


# In[33]:


for i in db.batsman_data.find({},{'_id':0}):
    print(i)


# In[35]:


#list of batsman
db.batsman_data.distinct('Batsman')


# In[34]:


a=db.batsman_data.aggregate([{"$group":{'_id':{'Batsman':"$Batsman",'Runs':"$Runs"},'count':{"$count":{}}}}])
for i in a:
    print(i)


# In[37]:


#count of 6s
a=db.batsman_data.aggregate([{"$group":{'_id':{'Batsman':"$Batsman",'6s':"$6s"},'count':{"$count":{}}}}])
for i in a:
    print(i)


# In[39]:


#count of 4s
a=db.batsman_data.aggregate([{"$group":{'_id':{'Batsman':"$Batsman",'4s':"$4s"},'count':{"$count":{}}}}])
for i in a:
    print(i)


# In[47]:


for i in db.batsman_data.find({},{'_id':0,'Batsman':1,"Runs":1}):
    print(i)


# In[41]:


db.bowler_data.count_documents({})


# In[42]:


for i in db.bowler_data.find({},{'_id':0}):
    print(i)


# In[44]:


#list of bowler
db.bowler_data.distinct('Bowler')


# In[45]:


a=db.bowler_data.aggregate([{"$group":{'_id':{'Bowler':"$Bowler",'wkts':"$Wkts"},'count':{"$count":{}}}}])
for i in a:
    print(i)


# In[48]:


for i in db.bowler_data.find({},{'_id':0,'Bowler':1,"Wkts":1}):
    print(i)


# In[ ]:




