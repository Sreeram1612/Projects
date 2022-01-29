#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient


# In[2]:


client = MongoClient('mongodb://localhost:27017/')


# In[3]:


client.list_database_names()


# In[4]:


db=client['Students']


# In[5]:


db.list_collection_names()


# In[7]:


for i in db.marks.find():
    print(i)


# In[11]:


#count no.of group "D"
for i in db.marks.find({},{"race/ethnicity":"group D"}):
    print(i)


# In[19]:


A=db.marks.count_documents({"race/ethnicity":"group A"})

B=db.marks.count_documents({"race/ethnicity":"group B"})

C=db.marks.count_documents({"race/ethnicity":"group C"})

D=db.marks.count_documents({"race/ethnicity":"group D"})

E=db.marks.count_documents({"race/ethnicity":"group E"})


print("Total count of students in Group A : ",A)

print("Total count of students in Group B : ",B)

print("Total count of students in Group C : ",C)

print("Total count of students in Group D : ",D)

print("Total count of students in Group E : ",E)


# In[23]:


#Total Average marks in data
a=db.marks.aggregate([{"$group":{"_id":0,"Average Marks":{"$avg":"$Total Marks"}}}])
for i in a:
    print (i)


# In[24]:


#maximum marks based on lunch
r=db.marks.aggregate([{"$group":{"_id":{"Student":"$gender","lunch":"$lunch","maxmarks":{"$max":"$Total Marks"}}}}])

for i in r:
    print(i)


# In[29]:


#separate marks by students
r=db.marks.aggregate([{"$group":{"_id":{"Student":"$gender","Maths":"$math score","Reading":"$reading score","Writing":"$writing score","Totalmarks":{"$max":"$Total Marks"}}}}])

for i in r:
    print(i)


# In[36]:


#students classified by scores

for i in db.marks.aggregate([{"$match":{"$and":[{"Average":{"$gte":75,"$lte":100}}]}},{"$project":{"_id":1,"Average Marks":"$Average"}}]):
    print("scored in first class",i)
for j in db.marks.aggregate([{"$match":{"$and":[{"Average":{"$gte":50,"$lte":75}}]}},{"$project":{"_id":1,"Average Marks":"$Average"}}]):
    print("scored in second class",j)
for k in db.marks.aggregate([{"$match":{"$and":[{"Average":{"$lte":50}}]}},{"$project":{"_id":1,"Average Marks":"$Average"}}]):
    print("scored in Third class",k)    


# In[74]:


#count of students classified by scores
a=db.marks.aggregate([{"$match": {"Average": {"$gt": 76}}},{"$count": "First Class"}])
b=db.marks.aggregate([{"$match": {"Average": {"$gt": 51,"$lt":75}}},{"$count": "Second Class"}])
c=db.marks.aggregate([{"$match": {"Average": {"$lt": 50}}},{"$count": "Third Class"}])
print("Students has been passed out 3 classes based on their marks: ")
for i in a:
    print(i)
for j in b:
    print(j)
for k in c:
    print(k)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




