'''
Ler dois números inteiros, executar e mostrar o resultado das seguintes operações:

Adição
Subtração
Multiplicação
Divisão

'''

#%%

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

print(f'A Adição de {num1} e {num2} é igual a: {num1 + num2}')
print(f'A Subtração de {num1} e {num2} é igual a: {num1 - num2}')
print(f'A Multiplicação de {num1} e {num2} é igual a: {num1 * num2}')
print(f'A Divisão de {num1} e {num2} é igual a: {num1 / num2}')
# %%

'''
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
'''

temp_viagem = int(input('Informe o tempo gasto na viagem: '))
velocidade_media = float(input('Informe a velocidade média'))
distancia = (temp_viagem * velocidade_media)
litros_usados = distancia / 12

print(f'Tempo gasto na viagem: {temp_viagem}\nVelocidade média: {velocidade_media}\nDistância percorrida: {distancia}\nQuantidade de litros utilizada na viagem: {litros_usados} litros')
# %%
