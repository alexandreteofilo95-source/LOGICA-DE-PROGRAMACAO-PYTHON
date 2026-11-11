import os
os.system('cls')
#função
def cabecalho():
    print('\n')
    print('=' *15)
    print('       SENAI')
    print('=' *15)
    return
#usando função.
cabecalho()
nome = input('digite seu nome: ')

cabecalho()#usando a função
idade = input('digite sua idade: ')

cabecalho()#usando a função
print(f'nome: {nome}')
print(f'idade: {idade}')