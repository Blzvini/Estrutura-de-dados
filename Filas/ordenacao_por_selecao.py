#%%

def buscaMenor(arr):
    menor = arr[0] # Armazena o menor valor.
    menor_indice = 0 # Armazena o índice de menor valor.
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice
    

def ordenacaoPorSelecao(arr): 
    novoArr = []
    for i in range(1, len(arr)):
        menor = buscaMenor(arr) # Encontra o menor elemento do arr e adiciona ao novo arr
        novoArr.append(arr.pop(menor))
    return novoArr    


# %%

lista = [5,3,6,2,10]

print(ordenacaoPorSelecao(lista))
# %%
