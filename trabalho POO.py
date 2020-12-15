#!/usr/bin/env python
# coding: utf-8

# In[144]:


#segunda ta worth
import random as  rd
class lista():
    def __init__(self):
        self.quantidade = []
        self.valorMinimo = []
        self.valorMaximo = []
    def listaAleatoria(self,quantidade,valorMinimo,valorMaximo):
        lista = []
        self.quantidade = quantidade
        self.valorMaximo = valorMaximo
        self.valorMinimo = valorMinimo
        for i in range(self.quantidade):
            lista.append(rd.randint(self.valorMinimo,self.valorMaximo))
        print("lista aleatoria: ")
        print(lista)
        Metade = len(lista)//2
        A = slice(0,Metade)
        B = slice(Metade,quantidade)
        print("primeira metade: ",lista[A],"segunda metade: ",lista[B])
        soma = sum(lista)
        media = soma/quantidade
        #printa só os acima da media
        C = []
        for i in range(len(lista)):
            if lista[i] > media:
                C.append(lista[i]) 
        print("Só os acima da média: ",C)
minhaLista = lista()
minhaLista.listaAleatoria(10,1,10)


# In[63]:


#terceira ta worth
import random 
class tarefas():
    def __init__(self):
        self.nomes = []
        self.tarefas = []
    def definirTarefas(self,nomes,tarefas):    
        self.nomes = nomes
        self.tarefas = tarefas
        random.shuffle(self.nomes)
        random.shuffle(self.tarefas)
        for i in range(len(self.tarefas)):
            print(self.nomes[i],"Devera",self.tarefas[i])
meusNomes = tarefas()
meusNomes.definirTarefas(["Anderson", "Zuleika", "Jorge", "Marta", "Mike"],["lavar a louça", "varrer o chão", "tirar o pó", "lavar o quintal", "cortar a grama"])


# In[2]:


#primeira ta worth
class Notas():
    
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        self.notas = []
    def setNota(self, nota):
        #Adicionar uma nota a lista self.notas
        self.notas.append(nota)
    def getMedia(self):
        #Retornar a media do aluno
        soma_das_notas= sum(self.notas)
        media = soma_das_notas/len(self.notas)
        self.media = media
        print("\nA media é:", media)
    def apresentarResultado(self):
        #Adicionar código
        # Apresentar resultados conforme saída abaixo.
        # Media mínima de aprovação igual seis (6). 
        # Media entre 4 e 6 aluno em recuperação. Media menor que 4 aluno reprovado
        print("Resultado final para o aluno",self.nome,"é: ")
        if self.media >= 6:
            print("Aprovado")
        elif self.media < 6 and self.media >=4 : 
            print("Em recuperação")
        elif self.media < 4:
            print("Reprovado")
    def salvarDados(self):
        # Salvar os dados em um arquivo texto conforme apresentado abaixo
        arquivo= open("Notas.txt","a") 
        arquivo.write("\nNome: "+str(self.nome))
        arquivo.write("\nDisciplina: "+str(self.disciplina))
        arquivo.write("\nNotas: "+str(self.notas))
        arquivo.write("\nMedia: "+str(self.media))
        arquivo.close()
notas = Notas("Humberto","Programação")
notas.setNota(5.5)
notas.setNota(8.0)
notas.setNota(7.5)
notas.getMedia()
notas.apresentarResultado()
notas.salvarDados()


# In[ ]:




