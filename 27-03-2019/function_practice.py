#!/usr/bin/env python
# coding: utf-8

# In[4]:


def check(s):
    if 'python' in s.lower():
        return True
    else:
        return False
check("Python is programming language")


# # Can also be written as

# In[6]:


def checks(s):
    return 'python' in s.lower()
checks("Python is programming language")


# # PIG LATIN 

# In[14]:


def pig_latin(st):
    if st[0] in 'aeiou':
        return st+'ay'
    else:
        return st[1:]+st[0]+'ay'

pig_latin("word")


# # *args

# In[16]:


def myfun(*args): # *args allow to pass as many argument as we want and args return tuple
    print(args)
    
myfun(1,2,3,4,5)


# In[17]:


def myfun1(*args):
    return sum(args)

myfun1(1,2,3,4,5)


# # **kwargs

# In[19]:


def myfun2(**kwargs):# **kwargs retun dictionary
    print(kwargs)

myfun2(fruit="apple",veggie="luttuce")


# In[24]:


def dic(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find my fruit here')
dic(fruit="apple",veggie="luttuce")


# # In combination of **args and ***kwargs

# In[25]:


def myfun3(*args,**kwargs):
    print(args)
    print(kwargs)
    
myfun3(10,20,30,fruit="apple",food='eggs',animal='Dogs')

