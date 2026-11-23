import os
os.system('cls')


while True:
    print('''                    == Menu de preços ==
CARRO: R$10
MOTO: R$12
MOTOR: R$30
BRINQUEDO: R$20
SANDALIA: R$15
''')
    escolha = input('escolha uma das opções: ').upper()
    match escolha:
        case 'CARRO' | 'carro':
            print('R$10')
            break
        case 'MOTO' | 'moto':
            print('R$12')
            break
        case 'MOTOR' | 'motor':
            print('R$30')
            break
        case 'BRINQUEDO' | 'brinquedo':
            print('R$20')
            break
        case 'SANDALIA' |'sandalia':
            print('R$15')
            break
        case _:
            print('escolha uma das opçoes do menu')
            input('aperte a tecla Enter para voltar...')
            os.system('cls')