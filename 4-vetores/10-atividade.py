import os
os.system('cls')
NUMEROS_TENTATIVAS = 5
numeros_vetore = []

for i in range(NUMEROS_TENTATIVAS):
    numero = int(input(f'digite {i+1}º numero: '))

    if numero < 0:
        numero = 0
    numeros_vetore.append(numero)

for indice, numero in enumerate (numeros_vetore, start=1):
    print(f'{indice}º) : {numero}')

    