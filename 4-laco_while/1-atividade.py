import os
os.system('cls')

while True:
    numero = int(input('digite um numero emtre 1 a 10: '))
    if numero < 1 or numero > 10:
        print('numero invalido, tente novamente!')
    else:
        print('O numero esta entre 1 e 10.')
        break #serve para  parar o laço de repetoção.

print('=fim=')