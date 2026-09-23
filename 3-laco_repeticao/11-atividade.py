import os
os.system('cls')

QUANTIDADE_REPETICOES = 4
pares = 0
impares = 0 
for i in range(QUANTIDADE_REPETICOES):
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Quantidade de pares: {pares}')
print(f'Quantidade de impares: {impares}')
print('fim')