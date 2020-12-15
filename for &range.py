#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(5):
    print(i)


# In[2]:


for i in range(5,10):
    print(i)


# In[3]:


for i in range(5,20,2):
    print(i)


# In[5]:


import random as rd
val1 = rd.random()*10
print(val1)
val2= rd.randint(10,30)
print(val2)


# In[6]:


lista= [5,6,7,4]
print (lista)


# In[7]:


lista.insert(2,9)
print (lista)


# In[8]:


lista.append(3)
print(lista)


# In[11]:


removido = lista.pop(1)
print(lista)
print(removido)


# In[ ]:




