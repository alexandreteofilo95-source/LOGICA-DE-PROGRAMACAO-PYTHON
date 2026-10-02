import os 
os.system('cls')
NUMEROS_REPETIÇOES = 3
soma = 0 
for i in range(NUMEROS_REPETIÇOES):
    while True:
        n = float(input(f'Digite a {i + 1}º nota: '))
        if soma < 0 and soma >10:
            print('numero invalidos!')
            input('Aperte Enter para tentar novamente...')
        elif soma >= 7:
            soma += n
            media = soma / NUMEROS_REPETIÇOES
            print(f'media: {media}')
            print('aprovado')
            break
        elif media >= 5 and media < 6.9:
            print(f'media: {media}')
            print('recuperação')
            break
        else:
            print(f'media: {media}')
            print('reprovado')
            break