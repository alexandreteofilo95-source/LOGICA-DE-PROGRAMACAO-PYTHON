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
    numero +=1

    match opcao:
        case 1:
            print('\n== CADASTRO ==')
        
            nome = input('digite seu nome completo: ')
            
            lista_cadastro.append(nome)
            if nome == '':
                print('coloque um nome ou sobrenome!')
            elif nome in lista_cadastro:
                print('adicionado a lista com sucesso!')
            else:
                lista_cadastro.append(nome)
                print('ja foi adicionado!')

        case 2:
            print('== AMOSTRANDO LISTAGEM')
            for cadastro in lista_cadastro:
             print(f'Seu cadastro: {cadastro} \nnumero para identificação: {len(lista_cadastro)}')

        case 3:
           print('== atualizar cadastro ==')
           nome = input('Qual cadastro você deseja atualizar: ')
           if nome in lista_cadastro:
               posicao = lista_cadastro.index(nome)
               novo = input('coloque um novo cadastro: ')
               lista_cadastro[posicao] = novo
               print('cadastro realizado com sucesso!')
           else: 
               print('cadastro não encontrado.')
        case 4:
            print('== Remover cadastro ==')
            nome = input('Qua cadastro você deseja remover: ')
            if nome in lista_cadastro:
             lista_cadastro.remove(nome)
             print('cadastro removido com sucesso!')
            else:
                print('cadastro não encontrado.')
        
