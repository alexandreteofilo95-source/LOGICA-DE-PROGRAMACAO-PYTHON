import os
os.system('cls')


lista_produtos = []

while True:
    os.system('cls')
    print('''
=== MERCADO DENDEZEIROS ===
1 - CADASTRA PRODUTO
2 - LIOSTA TODOS OS PRODUTOS
3 - ATUALIZAR PRODUTO
4 - ROMOVER PRODUTO
5 - BUSCAR POR PRODUTO
0 - SAIR
''')

    opcao = int(input('Escolha uma opção: '))

    match opcao:
        #CREATE(INSERIR)
        case 1:
            print('== CADASTRAR PRODUTO ==')
            nome_produto = input('Digite o nome do novo produto: ').strip().upper()
            if nome_produto == '':
                print('O nome do produto de ser inserido...')
            elif nome_produto in lista_produtos:
                print('Produto ja cadastrado')
            else:
                lista_produtos.append(nome_produto)
            
                print('produto cadastrado com sucesso!')

        case 2:
            #READ(LER / BUSACAR)
            print('== PRODUTOS NO ESTOQUE ==')
            for produto in lista_produtos:
                print(f'- {produto}')
            print(f'total: {len(lista_produtos)}')
            
        case 3:
            #UPDATE(ATUALIZAR)
            print('== ATUALIZAR PRODUTO ==')
            nome = input('Qual produto deseja atualizar?: ')
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input('novo nome: ')
                lista_produtos[posicao] = novo
                print('produto alterado com sucesso! ')
            else:
                print('produto não encotrado.')
            
        case 4:
            #DELETE(REMOVER)
            print('\n== REMOVER PRODUTO ==')
            nome = input('qual produto  deseja remover? ')
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print('produto excluido com sucesso!')
            else:
                print('produto não encotrado.')
            
        case 5:
            #READ(ler)
            print('\n== ESCONTRAR PRODUTO ==')
            nome = input('Qual produto deseja busacar? ')
            if nome in lista_produtos:
                print('produto encontrado!')
            else:
                print('este produto não encontrado!')

        case 0:
            print('Saindo do Programa...')
    input('presione um tecla para continuar...')