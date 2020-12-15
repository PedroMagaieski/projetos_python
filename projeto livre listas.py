#!/usr/bin/env python
# coding: utf-8

# In[3]:


lista = []
continuar = 'S'
cont=0
while continuar.upper() == 'S':
    cont+=1
    aluno=input("Digite o nome do aluno: ")
    lista.append(aluno)
    continuar=input("Deseja digitar o nome de outro aluno?  ('S' para sim): ")
print("\nTodos os alunos cadastrados:")
for i in range(len(lista)):
    print(lista[i])
alternativa = int(input("\nO que deseja fazer ? 1-inserir 2-editar 3-deletar 4-sair"))
if alternativa == 1:
    posicao = int(input("Digite a posição em que deseja inserir o aluno: "))
    insere = input("Digite o nome do aluno que deseja inserir: ")
    lista.insert(posicao,insere)
    print(lista)
elif alternativa == 2:
    posicao = int(input("Digite a posição do aluno que deseja editar: "))
    altera = input("Digite o nome que deseja colocar no lugar do anterior: ")
    lista[posicao] = altera
    print(lista)
elif alternativa == 3:
    posicao = int(input("Digite a posição do aluno que deseja deletar: "))
    del lista[posicao]
    print(lista)
else:
    print(lista)
    print("Fim do programa")


# In[ ]:




