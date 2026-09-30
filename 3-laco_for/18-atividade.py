import os
os.system('cls')
NUMEROS_REPETIDOS = 5
pares = 0
impares = 0
for i in range(NUMEROS_REPETIDOS):
    n = int(input('digite um numero inteiro: '))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'numeros pares repetidos: {pares}')
print(f'numeros impares repitidos: {impares}')