import os
os.system('cls')

while True:
    numero = int(input('digite sua nota: '))
    if numero < 0 or numero >10:
        print('invalido, digite uma numero de 1 a 10')
    else:
        print(f'\n  sua nota foi: {numero} ')
        break