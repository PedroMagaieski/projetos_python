#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Cachorro():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def sentar(self):
        print(self.nome + " está sentado")
    def latir(self):
        print(self.nome + " latiu!")
    def getDescricao(self):
        res = "O nome do cachorro é "+ self.nome + " ele tem "+ str(self.idade) + " anos de idade"
        return res
meuCachorro = Cachorro("Totó",3)
seuCachorro = Cachorro("spyke",1)
meuCachorro.nome = "otot"
print(meuCachorro.getDescricao())
print(seuCachorro.getDescricao())


# In[ ]:




