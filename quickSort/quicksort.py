#%%
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total

print(soma([1,2,3,4,5]))
# %%

""" Escreva uma função recursiva que conte o número de itens em uma lista."""

def recursiva(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + recursiva(lista[1:])
    
    
print(recursiva([]))
#print(recursiva([1,2,3,4,5]))
# %%
""" Encontre o valor mais alto em uma lista"""

def valorMaisAlto(lista):
    
    if not lista:
        return None
    elif len(lista) == 1:
        return lista[0]
    
    valMax = valorMaisAlto(lista[1:])
    if lista[0] > valMax:
        return lista[0]
    else:
        return valMax
    
print(valorMaisAlto([]))
# %%
