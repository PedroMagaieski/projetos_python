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

