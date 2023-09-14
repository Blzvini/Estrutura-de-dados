# Os dados estão organizados na ordem ascendente de valores-chave, ou seja, com o menor valor no índice 0 e cada célula mantendo um valor maior que a célula abaixo

# Vantagem: Agiliza os tempos de pesquisa

#[ 1 | 2 | 4 | 5 | 8 | | | ]

# Inserção
# Obrigatóriamente tem que manter a ordem dos dados, pesquisando antes de inserir um dado

#%%
import numpy as np


# %%
class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
    # O(n)
    def imprime(self):
        if(self.ultima_posicao == -1):
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao +1):
                print(i, ' - ', self.valores[i])
                
    # Inserir valores
    # O(n)
    def insere(self, valor):
        if(self.ultima_posicao == self.capacidade - 1):
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao +1):
            posicao = i
            if(self.valores[i] > valor):
                break
            if(i == self.ultima_posicao):
                posicao = i + 1
        
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x +1] = self.valores[x]
            x -= 1
            
        self.valores[posicao] = valor
        self.ultima_posicao += 1
        
    # Pesquisando valores
    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao +1):
            if(self.valores[i] > valor):
                return -1
            if(self.valores[i] == valor):
                return i 
            if(i == self.ultima_posicao):
                return -1
        
    # Excluindo valores
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
vetor = VetorOrdenado(10)
# %%
vetor.imprime()
# %%
vetor.insere(6)
# %%
vetor.imprime()
# %%
vetor.insere(4)
vetor.imprime()
# %%
vetor.insere(3)
vetor.imprime()
# %%
vetor.insere(5)
vetor.imprime()
# %%
vetor.insere(1)
vetor.imprime()
# %%
vetor.insere(8)
vetor.imprime()
# %%
vetor.pesquisar(5)
# %%
vetor.pesquisar(8)
# %%
vetor.pesquisar(2)
# %%
vetor.pesquisar(9)
# %%
vetor.excluir(5)
vetor.imprime()
# %%
vetor.excluir(1)
vetor.imprime()
# %%
vetor.excluir(8)
vetor.imprime()
# %%
vetor.excluir(9)

# %%
vetor.pesquisar(9)
# %%
