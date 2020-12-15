#!/usr/bin/env python
# coding: utf-8

# In[13]:


names = []
notes = []
idn = 'S'

def get_avarage(notes):
    return sum(notes) / len(notes)

def get_approved(notes):
    return [notes.index(note) for note in list(filter(lambda note: note >= 6, notes))]

def get_failed(notes):
    return [notes.index(note) for note in list(filter(lambda note: note < 6, notes))]

while idn == 'S' or idn == 's':
    names.append(input('Digite o nome do aluno: '))
    notes.append(int(input('Digite a nota do aluno: ')))
    idn = input('Deseja digitar a noda de outro aluno?  (\'S\' para sim): ')

print('\n\n')
for index in range(len(names)):
    print('* Aluno %s: %d' % (names[index], notes[index]))

print('\nA média da turma é: ', get_avarage(notes))

print('\nAprovados')
for index in get_approved(notes):
    print('- ', names[index])

print('\nReprovados')
for index in get_failed(notes):
    print('- ', names[index])
    
    


# In[8]:


alunos = []
notas = []
aprovados = []
reprovados = []
continuar = 'S'
cont = 0
while continuar.upper()=='S':
    cont+=1
    aluno = input("Digite o nome do aluno: ")
    alunos.append(aluno)
    nota = int(input("Digite a nota do aluno"))
    notas.append(nota)
    if(nota<6):
        reprovados.append(aluno)
    else:
        aprovados.append(aluno)
        
    continuar = input("Digite S se deseja digitar a nota de outro aluno: ")
    
print("Todos os alunos cadastrados: ")
for i in range(len(alunos)):
    print("%s: %s"%(alunos[i],notas[i]))

    print("\nA media da sala é: ",sum(notas)/cont)

print("\naprovados: ")
for i in aprovados:
    print(i)
print("\nreprovados")
for i in reprovados:
    print(i)
    
    


# In[ ]:




