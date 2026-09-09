import os
os.system('cls')

# ENTRADA
matricula = int(input('digite a sua matricula: '))
data = int(input('Qual sua data de nascimento: '))
ano = int(input('Quantos anos vc tem de trabalho: '))
soma = 2026 - data
# PROCESSAMENTO
if data >= 65 and ano >=30:
    print('Requerer à aposentadoria.')
else:
    print('Não requerer à aposentadoria.')

# SAIDA
