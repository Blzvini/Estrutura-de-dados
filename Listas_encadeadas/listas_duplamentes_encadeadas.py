# Lista duplamente encadeada

#%%

class No:
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None
        
    
    def mostra_no(self):
        print(self.valor)

# %%
class ListaDuplamenteEncadeada:
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def __lista_vazia(self):
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo
        
    def mostrar_lista_inicio_final(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo
            
    def mostrar_lista_final_inicio(self):
        atual = self.ultimo
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior
# %%
# Insere no início
lista = ListaDuplamenteEncadeada()

lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar_lista_inicio_final()
#%%
lista.primeiro, lista.ultimo
#%%
lista.primeiro.valor, lista.ultimo.valor
#%%
lista.mostrar_lista_final_inicio()
#%%
# Insere no final

#%%
# Excluir do início e do final