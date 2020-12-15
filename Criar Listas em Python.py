#!/usr/bin/env python
# coding: utf-8

# In[1]:


listas = [1,2,3,4,5]
listas.append(0)
print(listas)


# In[3]:


print(len(listas))


# In[4]:


listas.insert(2,7)
print(listas)


# In[7]:


valor= listas.pop(2)
print(valor)
print(listas)


# In[10]:


listas.sort()
print(listas)


# In[11]:


listas.reverse()
print(listas)


# In[13]:


lista2 = listas##errado
print(lista2)


# In[15]:


lista2[3]=0
print(lista2)


# In[16]:


print(listas)


# In[18]:


lista3 = listas[:]##certo
lista3[3]=9
print(lista3)
print(listas)


# In[19]:


compras = ['arroz','feijão','farinha','leite']
indx = compras.index('farinha')
##compras.sort()
#print(compras)
print(indx)
print(compras[indx])


# In[21]:


nome = ['Rosenildson', 'Jostrebaldo', 'Gertrudes']
RA =   [158,            123,           412]
setor= ["Manutenção", "Segurança", "Suporte"]

busca = int(input('entre com o RA do funcionario'))
indice = RA.index(busca)

print("o funcionario %s (RA: %s) trabalha no setor %s"%(nome[indice],RA[indice],setor[indice]))


# In[24]:


notas = [8,5,7,6]
menor = notas[0]
soma = 0
cont = 0
for i in notas :
    if i<menor:
        menor=i
maior = notas[0]
for i in notas: 
    if i>maior:
        maior = i
print("menor nota:", menor)
print("menor nota:", maior)
print("soma: ", soma)
##print("media", soma/cont)


# In[ ]:


notas = [8,5,7,6,4,10]
print("a menor nota é:",min(notas)
print("a menor nota é:",max(notas))
print("a soma das notas é", (notas))
print("a media é", len(notas))

