import os
os.system('cls')
while True:
    def logo_senai():
        print('='*15)
        print('      SENAI')
        print('='*15)
    def mostrar_dados():
        if nome == '':
            print('nenhum cadastro')
        else:    
            print(f'nome: {nome}, email: {email}, telefone: {telefone}')
    print('''
1-cadastrar
2-consultar
3-sair

''')
    escolha = int(input('escolha uma das opções: '))

    match escolha:
        case 1:
            logo_senai()
            print('\n = Solicitando dados =')
            nome = input('digite seu nome: ')
            email = input('digite seu email: ')
            telefone = input('digite seu telefone: ')
        case 2:
            logo_senai()
            print('\n = exibindo dados =')
            mostrar_dados()
        case 3:
            os.system('cls')
            exit()
        case _:
            print('opção invalida!')
            input('clique enter para voltar...')
            os.system('cls')



