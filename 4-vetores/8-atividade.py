import os
os.system('cls')
numeros_vetores = []
par = 0
impar = 0

print('= INSIRINDO NUMEROS NO VETOR =')
for i in range(6):
    numero = int(input(f'Digite {i+1}º numero: '))
    numeros_vetores.append(numero)
    if numero % 2 == 0:
        par +=1
    else:
        impar +=1
        
print('\n= EXIBINDO NUMEROS DO VETOR =')
for indice, i in enumerate (numeros_vetores, start=1):
    print(f'{indice}º: {i}')

print('\n= EXIBINDO NUMEROS PARES E IMPARES NO VETOR =')
print(f'pares: {par}')
print(f'impares: {impar}')
