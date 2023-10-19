#%%

def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)
 
num = int(input('Informe um número: '))    
print(f'O fatorial de {num} é: {fatorial(num)}')
# %%
