# %%

# Função 3

def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

lista1()
# %%

# Função 4

def lista2():
    return range(1000)

l = lista2()

for i in l:
    print(i)