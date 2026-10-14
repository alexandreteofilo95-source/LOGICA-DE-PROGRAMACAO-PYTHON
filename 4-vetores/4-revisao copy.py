import os
os.system('cls')

print('= INSERINDO NUMEROS NO VETOR =')

vetor_numeros = []

numero = int(input('Digite um numero: '))
vetor_numeros.append(numero)
numero = int(input('Digite um numero: '))
vetor_numeros.append(numero)
numero = int(input('Digite um numero: '))
vetor_numeros.append(numero)

print('\n= EXIBINDO NUMEROS DO VETOR =')
print(f'Primeira posição do vetor: {vetor_numeros[0]}')
print(f'Ultima posição do vetor: {vetor_numeros[2]}')
