#%%
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) -1
    tentativas = 0
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        tentativas += 1
        
        if chute == item:
            return meio, tentativas
        elif chute > item:
            alto = meio -1
        else:
            baixo = meio + 1
    return None, tentativas


def criar_lista(tamanho):
    lista = list(range(tamanho))
    return lista


def main():
    tamanho_lista = int(input('Informe o tamanho da lista: '))
    lista = criar_lista(tamanho_lista)

    item = int(input('Informe um número para ser buscado na lista: '))
    posicao, tentativas = pesquisa_binaria(lista, item)

    if posicao is not None:
        posicao += 1  # Adiciona 1 para torná-lo uma posição humana
        print(f"Item: {item} encontrado na posição {posicao} após {tentativas} tentativas.")
    else:
        print(f"Item {item} não encontrado após {tentativas} tentativas.")


# %%
main()
# %%
