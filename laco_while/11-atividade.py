import os
os.system('cls')
soma = 0
NUMEROS_REPETIÇOES = 2
for i in range(NUMEROS_REPETIÇOES):
    while True:
        n = float(input(f'Digite a sua {i + 1}º nota: '))
        if soma < 0 and soma > 10:
            print('NUMERO INVALIDO!')
            input('aperte Enter para digitar novamente...')
            os.system('cls')
        else:
            soma += n
            break
media = soma / NUMEROS_REPETIÇOES
print(f'media: {media}')