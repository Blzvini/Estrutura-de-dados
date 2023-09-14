# %%

import numpy as np
# %%


class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return

        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vaziza')
            return

        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos - 1]


# %%
fila = FilaPrioridade(5)
# %%
fila.primeiro()
# %%

# Ordem da fila: 30

fila.enfileirar(30)
fila.primeiro()
# %%

#  Ordem da fila: 50, 30

fila.enfileirar(50)
fila.primeiro()
# %%

#  Ordem da fila: 50, 30, 10
# Ordem de uma fila tradicional: 10, 50, 30

fila.enfileirar(10)
fila.primeiro()
# %%
fila.valores
# %%

# Fila tradicional: 40, 10, 50, 30
#  Ordem da fila: 50, 40, 30, 10
fila.enfileirar(40)
fila.primeiro()
# %%
fila.valores
# %%

# Fila tradicional: 20, 40, 10, 50, 30
#  Ordem da fila: 50, 40, 30, 20, 10
fila.enfileirar(20)
fila.primeiro()
# %%
fila.valores
# %%
fila.enfileirar(2)
# %%
fila.desenfileirar()
fila.primeiro()
# %%
fila.desenfileirar()
fila.primeiro()
# %%
fila.desenfileirar()
fila.primeiro()

# %%
fila.valores
# %%
fila.enfileirar(5)
fila.primeiro()
# %%
fila.valores
# %%
