#%%

import numpy as np

# Estrutura básica do vetor
class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
    # Função para imprimir os dados    
    # O(n)
    def imprime(self):
        if(self.ultima_posicao == -1):
            print('O vetor está vazio!')
        else:
            for i in range(self.ultima_posicao +1):
                print(i, ' - ', self.valores[i])
    
    # Inserção dos dados
    # O(1) - Função constante
    def insere(self, valor):
        if (self.ultima_posicao == self.capacidade -1):
            print('Capacidade máxima já foi atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
            
    # Pesquisar um elemento
    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao+1):
            if (valor == self.valores[i]):
                return i
        return -1
    
    # Excluir um elemento
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if (posicao == -1):
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao -= 1

        
# %%
vetor = VetorNaoOrdenado(5)

# %%
vetor.imprime()
# %%
vetor.insere(2)
# %%
vetor.imprime()
# %%
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
# %%
vetor.imprime()
# %%
vetor.insere(7)
# %%
vetor.ultima_posicao
# %%
vetor.pesquisar(8)
# %%
vetor.pesquisar(9)
# %%
vetor.excluir(5)
# %%
vetor.excluir(1)
# %%
vetor.imprime()
# %%
vetor.excluir(2)
# %%
vetor.imprime()
# %%
vetor.insere(5)
vetor.insere(1)
vetor.imprime()
# %%
