#!/usr/bin/env python
# coding: utf-8

# In[1]:


##fatiamento de listas
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = lista1[2:5]
print(lista2)


# In[2]:


lista3 = lista1[:6]
print(lista3)


# In[3]:


lista4 = lista1[4:]
print(lista4)


# In[4]:


lista5 = lista1[:8:2]
print(lista5)


# In[5]:


lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
print(lista[0:10])
print(lista[:10])
print(lista[:])


# In[6]:


lista6 = lista[::-1]
print(lista6)


# In[7]:


listaA = [1,2,3,4,5,6,7,8,9,10]
listaB = [11,12,13,14,15,16,17,18,19,20]
meuSlice = slice(2,7)
print(listaA[meuSlice])
print(listaB[meuSlice])


# In[11]:


nome = 'joão cleber'
for i in range(len(nome)):
    print(nome[i:])


# In[ ]:




