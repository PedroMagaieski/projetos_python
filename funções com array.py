#!/usr/bin/env python
# coding: utf-8

# In[1]:


def somar(num1,num2):
    return num1 + num2
print(somar(5,4))


# In[8]:


def mensagem(nome="visintante",sobrenome=""):
    print("seja bem vindo"+ " "+ nome + " " + sobrenome)
mensagem(nome='joao',sobrenome='cleber')


# In[15]:


def mensagem(nome):
    return nome,len(nome)
var1,var2 = mensagem('joao') 
print(var2)


# In[18]:


def mensagem(nome):
    return [nome,len(nome)]
print(mensagem("will")[0])


# In[20]:


def sanduiche(*ingredientes):
    return ingredientes
print(sanduiche("queijo","alface","molho especial"))


# In[ ]:




