import os
os.system('cls')
numeros_vetores = []

print('= INSIRINDO NUMEROS NO VETOR =')
for i in range(5):
    numero = float(input(f'Digite {i+1}º numero: '))
    numeros_vetores.append(numero)
    maior = max(numeros_vetores)
    menor = min(numeros_vetores)

print('\n= EXIBINDO NUMEROS DO VETOR =')
for indice, i in enumerate (numeros_vetores, start=1):
    print(f'{indice}º: {i}')

print('\n= EXIBINDO MAIOR E MENOR NUMEROS NO VETOR =')
print(f'maior nota: {maior}')
print(f'menor nota: {menor}')
