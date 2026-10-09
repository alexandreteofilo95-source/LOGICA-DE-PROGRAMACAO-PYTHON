import os
os.system('cls')

while True:
    n = int(input('Digite sua nota entre 0 a 10: '))
    if n < 0 or n > 10:
        print('nota invalida!')
        print('tente novamente! \n')
    else:
        print(f'nota {n}')
        break