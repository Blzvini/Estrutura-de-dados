#%%

# Função 1 - O(n)

def soma1(n):
    soma = 0
    for i in range(n+1):
        soma += i
        
    return soma

print(soma1(10))
# %%

# Função 2

def soma2(n):
    return (n * (n + 1)) / 2

print(soma2(10))

