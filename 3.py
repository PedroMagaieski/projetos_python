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