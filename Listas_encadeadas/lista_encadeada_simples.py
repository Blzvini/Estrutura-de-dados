#%%
import numpy as np
# %%
class No:
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
    def mostrar_no(self):
        print(self.valor)
# %%

class ListaEncadeada:
    
    def __init__(self):
        self.primeiro = None
        
    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def mostrar(self):
        if self.primeiro.proximo == None:
            print('A lista está vazia')
            return None
        
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo
            
    def excluir_inicio(self):
        if self.primeiro.proximo == None:
            print('A lista está vazia')
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
        
# Insere no início

#%%
lista = ListaEncadeada()
lista.insere_inicio(1)

#%%
lista.mostrar()

#%%

# Excluir do início

lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()

#%%
lista.excluir_inicio()
lista.mostrar()