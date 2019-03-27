#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in enumerate("Python"):
    print(i)


# In[3]:


for a,b in enumerate("Python"):
    print(a,b)


# In[4]:


for a,b in enumerate("Python"):
    print(f"At {a} there is {b}")


# In[7]:


my_list1=[1,2,3]
my_list2=['a','b','c']
for i in zip(my_list1,my_list2):
    print(i)


# In[9]:


my_list1=[1,2,3]
my_list2=['a','b','c']
for a,b in zip(my_list1,my_list2):
    print(a,b)


# In[11]:


zip(my_list1,my_list2)


# In[13]:


list(zip(my_list1,my_list2))

