#!/usr/bin/env python
# coding: utf-8

# In[6]:


def somar(*valores):
    resultado = 0
    for i in valores:
        resultado += i
    return resultado
print(somar(1,2,3,4,5))


# In[7]:


def multiplicar(*valores):
    resultado = 1
    for i in valores:
        resultado *= i
    return resultado
print(multiplicar(1,2,3,4,5))


# In[22]:


def expo(num1,num2):
    resultado = 1
    for i in range(num2):
        resultado *=num1
    return resultado
print(expo(2,3))


# In[ ]:





# In[ ]:




