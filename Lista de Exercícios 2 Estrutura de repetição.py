#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nota = 0
while nota>=0 and nota<=10:
    nota = int(input("Digite uma nota: "))
print("Nota invalida, programa finalizado")
    


# In[ ]:


lista = []
soma = 0
media = 0
for i in range(5):
    lista.append(int(input("Digite um numero: ")))
print("a soma dos numeros é: ", sum(lista))
print("a media dos numeros é", sum(lista)/5)


# In[ ]:


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
for i in range(num1+1,num2):
    print(i)


# In[ ]:


num1 = int(input("Digite a base: "))
num2 = int(input("Digite o expoente: "))
pot = num1**num2
print(pot)


# In[ ]:


lista2 = []
pares = []
impares = []
for i in range(20):
    valor = int(input("Digite um numero"))
    lista2.append(valor)
    if valor%2==0:
        pares.append(valor)
    else :
        impares.append(valor)
print("todos os numeros: ")
for i in range(20):
    print("%s"%lista2[i])
print("todos os numeros pares: ")
for i in pares:
    print(i)
print("todos os numeros impares: ")
for i in impares:
    print(i)


# 

# In[ ]:


nume1 = int(input("Digite um numero: "))
nume2 = int(input("Digite outro numero: "))
fato = 0
for i in range(num1+1,num2):
    fato *=i
print(fato)

