import os
os.system('cls')
numeros_vetores = []

print('= INSIRINDO NOTA DO VETOR =')
for i in range(3):
    numero = float(input(f'Digite {i+1}º nota: '))
    numeros_vetores.append(numero)

print('\n= EXIBINDO NOTA DO VETOR =')
for indice, i in enumerate (numeros_vetores, start=1):
    print(f'{indice}º: {i}')
