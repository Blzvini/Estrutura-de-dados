#%%
'''
Leia a idade do usuário e classifique-o em:
- Criança - 0 a 12 anos
- Adolescente - 13 a 17 anos
- Adulto - acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

'''

# Resolução ex 1

def verificar_idade():
    try:
        idade = int(input('Informe a sua idade: '))
        
        if idade < 0:
            print('Informe uma idade válida, por favor.')
        elif(idade <= 12):
            print('Você é uma criança ainda!')
        elif(idade <= 17):
            print('Você é um Adolescente')
        elif(idade >= 18):
            print('Você é um adulto')
    except ValueError as e:
        print(f"Erro: {e}")


verificar_idade()
#%%
'''

Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

'''
# Resolução ex 2

def calcular_media():
    try:
        n1 = float(input("Digite a nota da M1: "))
        n2 = float(input("Digite a nota da M2: "))
        n3 = float(input("Digite a nota da M3: "))
        
        media = (n1 + n2 + n3) / 3
        
        if media < 4:
            print('Você está reprovado...')
        elif media > 4.1 and media < 6:
            print('Você está de recuperação..')
        else:
            print('Você está aprovado')
    except ValueError as e:
        print(f'Erro: {e}')
        
calcular_media()

