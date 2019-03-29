#!/usr/bin/env python
# coding: utf-8

# In[39]:


x='Im Global'

def greet():
    
    x='Im Enclosing'
    
    def hello():
        
#         x='Im Local'
        
        print(x)
    
    hello()


# In[33]:


greet()


# In[40]:


greet()


# In[38]:


greet()


# In[44]:


y1=20

def myfun1(y1):
    
    print(y1)
    
    y1=50
    
    print(y1)


# In[45]:


myfun1(y1)


# In[46]:


print(y1)


# -------------------------------------

# In[47]:


y=20

def myfun():
    global y
    print(y)
    
    y=50
    
    print(y)


# In[48]:


print(y) # Attention here


# In[49]:


myfun()


# In[50]:


print(y) # Attention here then


# ## up there we change the value of global varible

# In[ ]:




