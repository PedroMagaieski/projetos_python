#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''
Faça um programa em Python que sorteie e armazene em uma lista 20 números inteiros entre 50 e 100 e:
* Armazene os números pares em uma lista PAR e os números ímpares em uma lista ÍMPAR;
* Imprima todas as listas
* Apresente o maior e o menor elemento da lista;
* Apresente a média de todos os valores;
'''
import random as rd
PAR = []
ÍMPAR = []
lista = []
for i in range(20):
    lista.append(rd.randint(50,100))
print("os numeros: ")
print(lista)    
for i in range(20):
    if lista[i]%2==0:
        PAR.append(lista[i])
    else:
        ÍMPAR.append(lista[i])
print("todos os numeros pares: ")
print(PAR)
print("todos os numeros impares: ")
print(ÍMPAR)
print("Menor elemento: ",min(lista))
print("Maior elemento: ",max(lista))
print("a media dos elementos: ",sum(lista)/20)


# In[ ]:





# In[ ]:





# In[ ]:




