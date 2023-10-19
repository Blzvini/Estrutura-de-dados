#%%
def regressiva(i):
    print(i)
    regressiva(i-1)


print(regressiva(1))

# %%

"""_summary_
    O caso recursivo é quando a função chama a sí mesma. O caso-base é quando a função não chama a si mesma novamente, de forma que o programa não se torne um loop infinito.
"""

def regressiva(i):
    print(i)
    if i <= 1: # Caso base
        return
    else:
        regressiva(i-1) # Caso recursivo
        
print(regressiva(10))
# %%
