#!/usr/bin/env python
# coding: utf-8

# In[4]:


candidatos = []
numeros = []
partidos = []
continuar = 'S';
cont=0
while continuar.upper() == 'S':
    cont+=1
    candidato = input("Digite o nome do candidato: ")
    candidatos.append(candidato)
    numero = int(input("Digite o numero do candidato "))
    numeros.append(numero)
    partido = input("Digite o partido do candidato ")
    partidos.append(partido)
    continuar = input("Deseja cadastrar outro candidato? ('S' para sim): ")
busca = int(input("Entre com o numero do candidato: "))
try:
    indice = numeros.index(busca)
    print(indice)
    print("candidato-%s -numero: %s -partido: %s"%(candidatos[indice],numeros[indice],partidos[indice]))
except:
    print("candidato não encontrado")


# In[ ]:





# In[ ]:




