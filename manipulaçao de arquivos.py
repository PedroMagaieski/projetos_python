#!/usr/bin/env python
# coding: utf-8

# In[1]:


arquivo= open("meuArquivo.txt","w")
texto = input("Digite")
arquivo.write("escrevendo...")
arquivo.close()


# In[14]:


path = "C:\\Users\\MP"
arquivo = open(path + "meuArquivo.txt","r")
matr = []
for linha in arquivo:
    listaArq = linha.split()
    matr.append(listaArq)
arquivo.close()


# In[9]:


arquivo= open("meuArquivo.txt","a")
texto = input("Digite")
arquivo.write(texto)
arquivo.close()


# In[ ]:





# In[ ]:




