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