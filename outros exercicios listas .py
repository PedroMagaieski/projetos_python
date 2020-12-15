#!/usr/bin/env python
# coding: utf-8

# In[1]:


##esse aqui ta ok
import random as rd
pares = []
impares = []
lista = []
for i in range(20):
    lista.append(rd.randint(10,30))
for i in range(20):
    if lista[i]%2==0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
print("os numeros: ")
print(lista)
print("todos os numeros pares: ")
print(pares)
print("todos os numeros impares: ")
print(impares)
print("a media dos elementos: ",sum(lista)/20)


# In[1]:


## esse aqui ta ok
pergunta = []
cont = 0
continuar = 1
while continuar != 0:
    res1 = input("Digite S se Telefonou para a vítima: ")
    pergunta.append(res1)
    if res1 == "S":
        cont +=1
    res2 = input("Digite S se Esteve no local do crime: ")
    pergunta.append(res2)
    if res2 == "S":
        cont +=1
    res3 = input("Digite S se Mora perto da vítima: ")
    pergunta.append(res3)
    if res3 == "S":
        cont +=1
    res4 = input("Digite S se Devia para a vítima: ")
    pergunta.append(res4)
    if res4 == "S":
        cont +=1
    res5 = input("Digite S se Já trabalhou com a vítima ")
    pergunta.append(res5)
    if res5 == "S":
        cont +=1
    continuar = int(input("Digite 0 para ter acesso aos resultados:"))
print(cont)
if cont == 2:
    print("Suspeito otario suspeito")
elif cont>=3 and cont<=4:
    print("cumplice")
elif cont == 5:
    print("culpado")
else:
    print("inocente")

    
    


# In[2]:


## esse aqui ta ok
notas = []
continuar = 0;
cont=0
while continuar != -1:
    cont+=1
    nota = int(input("Digite a nota do aluno: "))
    notas.append(nota)
    continuar = int(input("Digite um numero qualquer para continuar('-1' para parar): "))
print(notas)
soma = sum(notas)
media = sum(notas)/cont
print("A soma das notas: ", soma)
print("A Media das notas é: ", media)
print("As notas acima da média são: ")
for i in notas:
    if i > media:
        print(i)
print("As notas abaixo de 7 são: ")
for i in notas:
    if i < 7 :
        print(i)
notas.reverse()
print("A lista das notas ao contrario")
for i in range(len(notas)):
    print(notas[i])
print("Fim do programa")



# In[ ]:





# In[ ]:





# In[ ]:




