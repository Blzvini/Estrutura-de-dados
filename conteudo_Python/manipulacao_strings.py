#%%

# Manipulação de strings

a = 'casaco'
print(a)
# %%

# Transformando em Maiúscula
# Transformando em Minúscula

maiuscula = a.upper()
print(f'Antes do upper, {a} depois do upper {maiuscula}')

minuscula = maiuscula.lower()
print(f'Antes do lower {maiuscula}, depois do lower {minuscula}')
# %%

# Primeira letra em Maiúscula

firstWordUpper = a.capitalize()
print(firstWordUpper)
# %%
metade_palavra = a[0:3]
print(metade_palavra)
# %%
ultimas_letras = a[3:]
print(ultimas_letras)
# %%
b = a.replace('aco', 'inha')
print(a)
print(b)
# %%
c = a.replace('o', 'a')
print(c)
# %%
# Retorna a posição...
c.find('s')
# %%
# Retorna em qual posição encontra a primeira..
c.find('a')
# %%
# Se não encontrar, retorna -1 ...
c.find(b)
# %%

e = ' casaco '
print(len(e))
# %%
f = e.strip()
print(f)
# %%
len(f)
# %%
n1 = 14
n2 = 16
# %%
print(f'Dividindo {n1} por {n2}, o resultado é {n1/n2}')
# %%
