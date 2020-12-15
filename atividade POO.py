#!/usr/bin/env python
# coding: utf-8

# In[16]:


class conta():
    def __init__(self,nomeCliente,agencia,conta,saldo):
        self.nomeCliente = nomeCliente
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    def informarDadosConta(self):
        res = "\nnome:"+self.nomeCliente+"\nagencia:"+str(self.agencia)+"\nconta:"+str(self.conta)+"\nsaldo:"+str(self.saldo)
        return res
    def depositar(self,soma):
        self.saldo += soma
        return self.saldo
    def sacar(self,subtrai):
        self.saldo -= subtrai
        return self.saldo
    def verificarSaldo(self):
        res = "saldo:"+ str(self.saldo)
        return res
conta1 = conta("lucao",45,123,0)
print(conta1.depositar(44))


# In[ ]:





# In[ ]:




