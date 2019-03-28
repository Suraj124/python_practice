#!/usr/bin/env python
# coding: utf-8

# In[1]:


def square(n):
    return n**2


# In[2]:


my_list = [1,2,3,4,5]


# In[5]:


for i in map(square,my_list):
       print(i)


# In[6]:


list(map(square,my_list))


# In[8]:


def splicer(s):
    if len(s)%2==0:
        return 'EVEN'
    else:
        return s[0]


# In[10]:


my_string_list=['Suraj','Tarun','Piyush','Ankit','Anjesh','William']


# In[11]:


list(map(splicer,my_string_list))


# In[13]:


def check_vowel(num):
    return num%2==0


# In[14]:


my_list1=[1,2,3,4,5,6]


# In[15]:


list(filter(check_vowel,my_list1))


# In[17]:


for i in filter(check_vowel,my_list1):
    print(i)


# # Lambda Expression

# In[18]:


list(map(lambda n:n**2,[1,2,3,4,5]))


# In[20]:


list(filter(lambda n: n%2==0,[1,2,3,4,5,6,7,8]))


# In[22]:


list(map(lambda name:name[0],my_string_list))


# In[30]:


" ".join(list(map(lambda name:name[0],my_string_list)))


# In[24]:


list(map(lambda name:name[::-1],my_string_list))


# In[ ]:




