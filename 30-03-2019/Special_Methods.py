#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Book():
    def __init__(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
    
    def __str__(self):
        return (f"{self.name} by {self.author}")
    def __len__(self):
        return self.pages
    def __del__(self):
        print('The object of book has been deleted')


# In[11]:


b=Book('Python','James',500)


# In[12]:


print(b)


# In[13]:


len(b)


# In[14]:


del b


# In[ ]:




