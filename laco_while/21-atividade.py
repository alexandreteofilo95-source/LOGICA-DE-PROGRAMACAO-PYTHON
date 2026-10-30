import os
os.system('cls')
lista_cadastro = []
vetores_cadastro = []
numero = 0
while True:
    
    print('''
1 - CADASTRO
2 - LISTAGEM
3 - ATUALIZAÇÃO
4 - REMOÇAO DO CADASTRO
5 - SAIR
''')
    opcao = int(input('escola uma opção: '))

    match opcao:
        case 1:
            print('\n== CADASTRO ==')
        
            nome = input('digite seu nome completo: ').strip().upper()
            
            numero +=1
            vetores_cadastro.append(numero)
            if nome == '':
                print('coloque um nome ou sobrenome!')
            elif nome in lista_cadastro:
                print('JA FOI ADICIONADO NA LISTA!')
            else:
                lista_cadastro.append(nome)
                print('ADICIONADO A LISTA COM SUCESSO!')

        case 2:
            print('== AMOSTRANDO LISTAGEM')
            for produto in lista_cadastro:
                    print(f'- {produto}')
                    print(f'numero para identificação: {len(lista_cadastro)}')
    